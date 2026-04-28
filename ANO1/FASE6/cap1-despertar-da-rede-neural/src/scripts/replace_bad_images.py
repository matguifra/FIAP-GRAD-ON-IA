"""Replace dataset images that still have empty labels with freshly-downloaded ones.

Quinta etapa do pipeline (último recurso). Roda APÓS fill_missing_labels.py.

Para cada label que ainda está vazio:
  1. Procura uma imagem candidata no HF (COCO train para vacas, cats_vs_dogs para cães).
  2. Roda YOLOv5l @ 1280 e exige pelo menos uma bbox da classe esperada (conf >= 0.25).
  3. Se passar no critério, sobrescreve a imagem (mesmo nome de arquivo) e escreve o label.

Por que sobrescrever em vez de só adicionar?
- O split 32/4/4 é fixo (split_dataset.py). Se removermos uma imagem teríamos que
  re-rodar o split inteiro, perder o seed e quebrar a reprodutibilidade. Mantendo o
  nome estável, o split intacto e só trocando o conteúdo, todo o resto do pipeline
  continua válido.

Por que conf=0.25 aqui (e não 0.05 como no fill_missing)?
- No fill estamos teimando com uma imagem que já existe; aceitamos detecção fraca.
- Aqui estamos ESCOLHENDO uma imagem nova entre milhares — então só queremos imagens
  onde o detector tem confiança alta. Imagens "fáceis" produzem labels mais limpos.
"""
from __future__ import annotations

from pathlib import Path

import torch
from datasets import load_dataset
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
RAW = ROOT / "raw_downloads"

COCO_COW_ID = 19
COCO_DOG_ID = 16
COCO_TO_OURS = {COCO_COW_ID: 0, COCO_DOG_ID: 1}

CONF = 0.25       # mais rigoroso: só queremos imagens onde o detector tem certeza
IOU = 0.45
MIN_SIZE = 300    # mesmo filtro de qualidade dos scripts de download


def find_empty_labels() -> list[tuple[Path, Path, int]]:
    """Varre os três splits e retorna (img_path, lbl_path, expected_class) dos vazios.

    A classe esperada é inferida do prefixo do nome (cow_/dog_) — depende dessa convenção.
    """
    out = []
    for split in ["train", "val", "test"]:
        lbl_dir = DATASET / split / "labels"
        img_dir = DATASET / split / "images"
        for lbl in sorted(lbl_dir.glob("*.txt")):
            if lbl.stat().st_size > 0:
                continue
            img_path = img_dir / f"{lbl.stem}.jpg"
            if lbl.stem.startswith("cow"):
                expected = 0
            elif lbl.stem.startswith("dog"):
                expected = 1
            else:
                continue
            out.append((img_path, lbl, expected))
    return out


def detect_and_format(model, img: Image.Image, expected: int, size: int = 1280) -> list[str]:
    """Roda inferência e retorna as linhas de label da classe esperada (já formatadas)."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    res = model(img, size=size)
    # Filtra só a classe COCO de interesse (cow OU dog, não os dois ao mesmo tempo).
    coco_target = COCO_COW_ID if expected == 0 else COCO_DOG_ID
    lines = []
    for *xyxy, conf, cls in res.xyxy[0].tolist():
        if int(cls) != coco_target:
            continue
        # Mesma conversão xyxy -> xywh normalizado dos outros scripts.
        x1, y1, x2, y2 = xyxy
        xc = ((x1 + x2) / 2) / w
        yc = ((y1 + y2) / 2) / h
        bw = (x2 - x1) / w
        bh = (y2 - y1) / h
        lines.append(f"{expected} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")
    return lines


def save_image(img: Image.Image, dst: Path) -> None:
    """Sobrescreve a imagem original mantendo o mesmo nome (preserva o split fixo)."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(dst, "JPEG", quality=92)


def replace_cow(missing: list[tuple[Path, Path, int]], model) -> int:
    """Stream COCO train (split diferente do val onde já pegamos as 40 originais)."""
    need = [m for m in missing if m[2] == 0]
    if not need:
        return 0
    print(f"Precisamos repor {len(need)} vacas. Streaming detection-datasets/coco (train split)...")
    # Importante: usamos o split 'train' aqui pra não cair nas mesmas imagens do
    # redownload_cows.py (que usou 'val'). Evita repetição visual no dataset.
    ds = load_dataset("detection-datasets/coco", split="train", streaming=True)

    used_names = {p.stem for p in (RAW / "cow").glob("*.jpg")}

    replaced = 0
    for row in ds:
        if not need:
            break
        if COCO_COW_ID not in row["objects"]["category"]:
            continue
        img = row["image"]
        if img.width < MIN_SIZE or img.height < MIN_SIZE:
            continue
        # Roda o detector ANTES de salvar — se não detectar nada, descarta a candidata.
        lines = detect_and_format(model, img, expected=0, size=1280)
        if not lines:
            continue

        # Anti-duplicata: image_id é a chave única do COCO. Construímos uma string
        # estável e checamos contra os nomes já existentes em raw_downloads/cow.
        stable_key = f"cow_img_{row['image_id']}"
        if stable_key in used_names:
            continue

        # Pop FIFO: a primeira imagem vazia é a primeira a ser reposta.
        img_path, lbl_path, _ = need.pop(0)
        save_image(img, img_path)
        lbl_path.write_text("\n".join(lines) + "\n")
        replaced += 1
        print(f"  reposta: {img_path.relative_to(ROOT)}  ({len(lines)} bbox)")
    return replaced


def replace_dog(missing: list[tuple[Path, Path, int]], model) -> int:
    """Stream cats_vs_dogs pulando o início (já consumido em download_images.py)."""
    need = [m for m in missing if m[2] == 1]
    if not need:
        return 0
    print(f"Precisamos repor {len(need)} cachorros. Streaming microsoft/cats_vs_dogs...")
    ds = load_dataset(
        "microsoft/cats_vs_dogs", split="train", streaming=True, trust_remote_code=True
    )
    # cats_vs_dogs não tem image_id estável; pulamos os primeiros 5000 itens pra evitar
    # cair em qualquer um dos 40 que download_images.py já pegou. Heurística simples mas eficaz.
    skip = 5000
    idx = 0
    replaced = 0
    for row in ds:
        if not need:
            break
        idx += 1
        if idx < skip:
            continue
        if row.get("labels") != 1:  # 1 = dog (mesma convenção do download_images.py)
            continue
        img = row["image"]
        if img.width < MIN_SIZE or img.height < MIN_SIZE:
            continue
        lines = detect_and_format(model, img, expected=1, size=1280)
        if not lines:
            continue

        img_path, lbl_path, _ = need.pop(0)
        save_image(img, img_path)
        lbl_path.write_text("\n".join(lines) + "\n")
        replaced += 1
        print(f"  reposto: {img_path.relative_to(ROOT)}  ({len(lines)} bbox)")
    return replaced


def main() -> None:
    missing = find_empty_labels()
    if not missing:
        # Caso ideal: fill_missing_labels.py já resolveu tudo.
        print("Nada a repor — todos os labels já preenchidos.")
        return
    print(f"Imagens a repor: {len(missing)}")
    for p, _, c in missing:
        print(f"  {p.relative_to(ROOT)} (classe esperada: {'cow' if c == 0 else 'dog'})")

    print("\nCarregando yolov5l @ 1280...")
    model = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True, trust_repo=True)
    model.conf = CONF
    model.iou = IOU
    model.classes = [COCO_COW_ID, COCO_DOG_ID]

    r_cow = replace_cow(missing, model)
    r_dog = replace_dog(missing, model)
    print(f"\nResumo: vacas repostas={r_cow}, cachorros repostos={r_dog}")

    # Verificação final: se algo ainda estiver vazio, o operador precisa intervir manual.
    remaining = find_empty_labels()
    if remaining:
        print(f"Ainda vazias: {len(remaining)}")
        for p, _, _ in remaining:
            print(f"  {p.relative_to(ROOT)}")
    else:
        print("Todos os labels agora estão preenchidos.")


if __name__ == "__main__":
    main()

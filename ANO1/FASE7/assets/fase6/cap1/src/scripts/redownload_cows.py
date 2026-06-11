"""Download 40 real cow images from COCO 2017 val split via HuggingFace (streaming).

Versão definitiva da coleta de vacas (substitui a tentativa de download_images.py via
Francesco/animals-ij5d2, que retornava muitos animais não-vaca).

A taxonomia COCO 2017 tem 80 classes; em detection-datasets/coco a classe 'cow' aparece
com id=19 (não confundir com o id=21 do COCO original — o HF usa indexação 0..79 sem
gaps). Streamamos o split de validação até acumular 40 imagens cuja anotação contenha
pelo menos uma instância de vaca.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from datasets import load_dataset
from PIL import Image

# Caminhos relativos ao próprio script — não dependem do diretório de execução.
ROOT = Path(__file__).resolve().parent.parent
FINAL = ROOT / "raw_downloads" / "cow"

TARGET = 40                    # 32 train + 4 val + 4 test
MIN_SIZE = 300                 # filtra imagens minúsculas (qualidade ruim no YOLO @ 640)
COCO_COW_CATEGORY_ID = 19      # id da classe 'cow' em detection-datasets/coco (HF, 0-indexed)


def save(img: Image.Image, path: Path) -> None:
    """Salva como JPEG RGB. YOLOv5 não aceita imagens com transparência ou modo L."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(path, "JPEG", quality=92)


def main() -> None:
    # Limpa execuções anteriores: garante reprodutibilidade total mesmo se rodar 2x.
    if FINAL.exists():
        shutil.rmtree(FINAL)
    FINAL.mkdir(parents=True, exist_ok=True)

    print("Abrindo COCO val (streaming) via HF detection-datasets/coco...")
    # streaming=True evita baixar o split inteiro (~5k imagens, vários GB).
    ds = load_dataset("detection-datasets/coco", split="val", streaming=True)

    kept = 0       # quantas imagens já salvamos
    scanned = 0    # quantas imagens do COCO foram inspecionadas (para diagnóstico)
    for row in ds:
        scanned += 1
        # Cada row tem 'objects.category' = lista de class ids das anotações daquela imagem.
        # Mantemos a imagem se houver pelo menos uma vaca anotada.
        cats = row.get("objects", {}).get("category", [])
        if COCO_COW_CATEGORY_ID not in cats:
            continue
        img = row["image"]
        if img.width < MIN_SIZE or img.height < MIN_SIZE:
            continue
        save(img, FINAL / f"cow_{kept:03d}.jpg")
        kept += 1
        if kept % 5 == 0:
            print(f"  {kept}/{TARGET} (escaneadas {scanned})")
        if kept >= TARGET:
            break

    print(f"\nTotal: {kept} imagens de vaca salvas em {FINAL} (escaneadas {scanned}).")
    if kept < TARGET:
        # Em geral o val do COCO tem >150 imagens com vaca, então 40 cabe folgado.
        # Se o dataset HF mudar de schema isso pode quebrar — fail-fast.
        raise SystemExit(f"ERRO: só consegui {kept}/{TARGET}.")


if __name__ == "__main__":
    main()

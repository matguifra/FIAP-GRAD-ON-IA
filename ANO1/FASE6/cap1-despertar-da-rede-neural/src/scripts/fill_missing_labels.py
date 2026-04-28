"""Try to label any remaining empty label files using a stronger model (yolov5l at 1280).

Quarta etapa (fallback) — só roda nas imagens cujo .txt ficou VAZIO depois do auto_label.py.

Estratégia em cascata:
  1. auto_label.py:        YOLOv5s @ 640 px, conf=0.15  (rápido, pega o caso fácil)
  2. fill_missing_labels:  YOLOv5l @ 1280 px, conf=0.05 (este script — pesado, mais sensível)
  3. replace_bad_images:   troca a imagem por outra do HF se nem o passo 2 detectar nada

Por que `yolov5l` em vez de `yolov5s`?
- yolov5l (~46M params) é ~6x maior que yolov5s (~7M) e captura objetos pequenos / parciais
  com muito mais precisão. O custo é só ~2-3s a mais por imagem, irrelevante em 80 fotos.

Por que size=1280?
- YOLOv5 escala detecções com a resolução de entrada. Vacas distantes em paisagem aberta
  podem ocupar <50px na imagem original; em 640 elas viram <30px e o detector ignora.
  Em 1280 dobra o número de pixels do objeto e o recall sobe muito.

Por que conf=0.05 (super permissivo)?
- Estas são as imagens "difíceis" — qualquer detecção da classe esperada é bem-vinda.
  O filtro semântico (classe = nome do arquivo) ainda elimina falso positivo de outra classe.
"""
from __future__ import annotations

from pathlib import Path

import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
SPLITS = ["train", "val", "test"]

# Mesma taxonomia do auto_label.py — mantida explícita aqui para o script ser auto-contido.
COCO_COW_ID = 19
COCO_DOG_ID = 16
COCO_TO_OURS = {COCO_COW_ID: 0, COCO_DOG_ID: 1}

CONF = 0.05  # muito permissivo, só para imagens difíceis — ver docstring acima
IOU = 0.45


def expected_class(image_path: Path) -> int:
    """Mesma lógica do auto_label.py: classe esperada inferida do prefixo do arquivo."""
    name = image_path.stem.lower()
    if name.startswith("cow"):
        return 0
    if name.startswith("dog"):
        return 1
    return -1


def main() -> None:
    print("Carregando yolov5l @ 1280 (modo fallback)...")
    # yolov5l é ~6x maior que yolov5s — o checkpoint pesa ~89MB no primeiro download.
    model = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True, trust_repo=True)
    model.conf = CONF
    model.iou = IOU
    model.classes = [COCO_COW_ID, COCO_DOG_ID]

    still_empty: list[Path] = []  # imagens que continuam sem detecção mesmo aqui
    filled = 0
    for split in SPLITS:
        img_dir = DATASET / split / "images"
        lbl_dir = DATASET / split / "labels"
        for lbl in sorted(lbl_dir.glob("*.txt")):
            # Só processamos labels VAZIOS — não sobrescrevemos os que auto_label.py já preencheu.
            if lbl.stat().st_size > 0:
                continue
            img_path = img_dir / f"{lbl.stem}.jpg"
            if not img_path.exists():
                continue
            expected = expected_class(img_path)
            with Image.open(img_path) as im:
                w, h = im.size
                res = model(im, size=1280)  # 2x a resolução padrão = melhor recall
            lines = []
            for *xyxy, conf, cls in res.xyxy[0].tolist():
                mapped = COCO_TO_OURS.get(int(cls))
                if mapped is None:
                    continue
                if expected != -1 and mapped != expected:
                    continue
                # Mesma conversão xyxy -> xywh normalizado do auto_label.py.
                x1, y1, x2, y2 = xyxy
                xc = ((x1 + x2) / 2) / w
                yc = ((y1 + y2) / 2) / h
                bw = (x2 - x1) / w
                bh = (y2 - y1) / h
                lines.append(f"{mapped} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")
            if lines:
                lbl.write_text("\n".join(lines) + "\n")
                filled += 1
                print(f"  preenchida: {split}/{lbl.stem} ({len(lines)} det.)")
            else:
                # Vai para a fila do replace_bad_images.py — substituição da imagem.
                still_empty.append(img_path)

    print(f"\nPreenchidas: {filled} | ainda vazias: {len(still_empty)}")
    if still_empty:
        print("Imagens sem detecção mesmo com yolov5l@1280:")
        for p in still_empty:
            print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

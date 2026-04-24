"""Try to label any remaining empty label files using a stronger model (yolov5l at 1280).

Only touches files that are currently empty. Does NOT overwrite non-empty labels.
"""
from __future__ import annotations

from pathlib import Path

import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
SPLITS = ["train", "val", "test"]

COCO_COW_ID = 19
COCO_DOG_ID = 16
COCO_TO_OURS = {COCO_COW_ID: 0, COCO_DOG_ID: 1}

CONF = 0.05  # muito permissivo, só para imagens difíceis
IOU = 0.45


def expected_class(image_path: Path) -> int:
    name = image_path.stem.lower()
    if name.startswith("cow"):
        return 0
    if name.startswith("dog"):
        return 1
    return -1


def main() -> None:
    print("Carregando yolov5l @ 1280 (modo fallback)...")
    model = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True, trust_repo=True)
    model.conf = CONF
    model.iou = IOU
    model.classes = [COCO_COW_ID, COCO_DOG_ID]

    still_empty: list[Path] = []
    filled = 0
    for split in SPLITS:
        img_dir = DATASET / split / "images"
        lbl_dir = DATASET / split / "labels"
        for lbl in sorted(lbl_dir.glob("*.txt")):
            if lbl.stat().st_size > 0:
                continue
            img_path = img_dir / f"{lbl.stem}.jpg"
            if not img_path.exists():
                continue
            expected = expected_class(img_path)
            with Image.open(img_path) as im:
                w, h = im.size
                res = model(im, size=1280)
            lines = []
            for *xyxy, conf, cls in res.xyxy[0].tolist():
                mapped = COCO_TO_OURS.get(int(cls))
                if mapped is None:
                    continue
                if expected != -1 and mapped != expected:
                    continue
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
                still_empty.append(img_path)

    print(f"\nPreenchidas: {filled} | ainda vazias: {len(still_empty)}")
    if still_empty:
        print("Imagens sem detecção mesmo com yolov5l@1280:")
        for p in still_empty:
            print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

"""Diagnostic: run YOLOv5s at low confidence on all raw images and report detected COCO classes per file.

Helps verify whether raw_downloads actually contains cows and dogs, or if the download
pipeline returned other animals. Prints a table.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw_downloads"


def main() -> None:
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, trust_repo=True)
    model.conf = 0.10
    model.iou = 0.45
    names = model.names

    for class_name in ("cow", "dog"):
        imgs = sorted((RAW / class_name).glob("*.jpg"))
        coco_counter: Counter[str] = Counter()
        no_det = 0
        for p in imgs:
            with Image.open(p) as im:
                res = model(im, size=640)
            detected = [names[int(c)] for *_, c in res.xyxy[0].tolist()]
            if not detected:
                no_det += 1
            else:
                coco_counter.update(set(detected))
        print(f"\n== {class_name} ({len(imgs)} imagens) ==")
        print(f"sem detecção: {no_det}")
        print("classes COCO detectadas (imagens contendo a classe):")
        for cls, n in coco_counter.most_common(15):
            print(f"  {cls}: {n}")


if __name__ == "__main__":
    main()

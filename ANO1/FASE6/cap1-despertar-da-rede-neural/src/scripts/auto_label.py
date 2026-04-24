"""Generate YOLO-format labels for every image in dataset/{train,val,test}/images.

Uses a COCO-pretrained YOLOv5s model. COCO already has `cow` (id 19) and `dog` (id 16),
so this gives high-quality pseudo-labels without manual annotation. Output labels use
our custom mapping: cow=0, dog=1.

Each label file is named like its image, with one line per detection:
    <class_id> <x_center> <y_center> <width> <height>   (all normalized to [0,1])

Images without a confident detection still get an empty .txt file so YOLOv5 does not
flag them as missing. Confidence threshold is configurable.
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

CONF_THRESHOLD = 0.15
IOU_THRESHOLD = 0.45


def load_model():
    print("Carregando YOLOv5s pré-treinado (COCO)...")
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, trust_repo=True)
    model.conf = CONF_THRESHOLD
    model.iou = IOU_THRESHOLD
    model.classes = [COCO_COW_ID, COCO_DOG_ID]
    return model


def expected_class_from_name(image_path: Path) -> int:
    """Infer intended class from filename prefix — our raw files are `cow_NNN.jpg` / `dog_NNN.jpg`."""
    name = image_path.stem.lower()
    if name.startswith("cow"):
        return 0
    if name.startswith("dog"):
        return 1
    return -1


def label_split(split: str, model) -> tuple[int, int, int]:
    img_dir = DATASET / split / "images"
    lbl_dir = DATASET / split / "labels"
    lbl_dir.mkdir(parents=True, exist_ok=True)

    images = sorted(img_dir.glob("*.jpg"))
    with_detection = 0
    empty = 0

    for img_path in images:
        expected_cls = expected_class_from_name(img_path)
        with Image.open(img_path) as im:
            w, h = im.size
            results = model(im, size=640)

        lines = []
        for *xyxy, conf, cls in results.xyxy[0].tolist():
            mapped = COCO_TO_OURS.get(int(cls))
            if mapped is None:
                continue
            if expected_cls != -1 and mapped != expected_cls:
                continue
            x1, y1, x2, y2 = xyxy
            xc = ((x1 + x2) / 2) / w
            yc = ((y1 + y2) / 2) / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
            lines.append(f"{mapped} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

        lbl_path = lbl_dir / f"{img_path.stem}.txt"
        lbl_path.write_text("\n".join(lines) + ("\n" if lines else ""))

        if lines:
            with_detection += 1
        else:
            empty += 1

    print(f"  {split}: {len(images)} imagens | com detecção: {with_detection} | sem detecção: {empty}")
    return len(images), with_detection, empty


def main() -> None:
    model = load_model()
    totals = {"images": 0, "detected": 0, "empty": 0}
    for split in SPLITS:
        n, d, e = label_split(split, model)
        totals["images"] += n
        totals["detected"] += d
        totals["empty"] += e
    print(
        "\nResumo:"
        f" total={totals['images']} com_detecção={totals['detected']} sem_detecção={totals['empty']}"
    )
    print("Labels salvos em dataset/{split}/labels/*.txt (classes: 0=cow, 1=dog)")


if __name__ == "__main__":
    main()

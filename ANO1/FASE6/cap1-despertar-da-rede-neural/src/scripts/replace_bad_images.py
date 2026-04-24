"""Replace dataset images that still have empty labels with freshly-downloaded ones.

For each empty-label file under dataset/{split}/labels/:
  1. Pull a candidate from HF (detection-datasets/coco for cows, microsoft/cats_vs_dogs for dogs).
  2. Run YOLOv5l @ 1280 and verify at least one bbox of the expected class.
  3. Overwrite the image AND write the label in YOLO format (class 0=cow, 1=dog).

Skips already-used image_ids/filenames by keeping an exclusion set based on the current
images in raw_downloads/.
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

CONF = 0.25
IOU = 0.45
MIN_SIZE = 300


def find_empty_labels() -> list[tuple[Path, Path, int]]:
    """Return list of (image_path, label_path, expected_class_id)."""
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
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    res = model(img, size=size)
    coco_target = COCO_COW_ID if expected == 0 else COCO_DOG_ID
    lines = []
    for *xyxy, conf, cls in res.xyxy[0].tolist():
        if int(cls) != coco_target:
            continue
        x1, y1, x2, y2 = xyxy
        xc = ((x1 + x2) / 2) / w
        yc = ((y1 + y2) / 2) / h
        bw = (x2 - x1) / w
        bh = (y2 - y1) / h
        lines.append(f"{expected} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")
    return lines


def save_image(img: Image.Image, dst: Path) -> None:
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(dst, "JPEG", quality=92)


def replace_cow(missing: list[tuple[Path, Path, int]], model) -> int:
    need = [m for m in missing if m[2] == 0]
    if not need:
        return 0
    print(f"Precisamos repor {len(need)} vacas. Streaming detection-datasets/coco (train split)...")
    ds = load_dataset("detection-datasets/coco", split="train", streaming=True)

    # evita reusar ids já baixados. image_id é único por imagem COCO.
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
        lines = detect_and_format(model, img, expected=0, size=1280)
        if not lines:
            continue

        # evita duplicata exata (nem sempre dá para saber, usamos image_id)
        stable_key = f"cow_img_{row['image_id']}"
        if stable_key in used_names:
            continue

        img_path, lbl_path, _ = need.pop(0)
        save_image(img, img_path)
        lbl_path.write_text("\n".join(lines) + "\n")
        replaced += 1
        print(f"  reposta: {img_path.relative_to(ROOT)}  ({len(lines)} bbox)")
    return replaced


def replace_dog(missing: list[tuple[Path, Path, int]], model) -> int:
    need = [m for m in missing if m[2] == 1]
    if not need:
        return 0
    print(f"Precisamos repor {len(need)} cachorros. Streaming microsoft/cats_vs_dogs...")
    ds = load_dataset(
        "microsoft/cats_vs_dogs", split="train", streaming=True, trust_remote_code=True
    )
    skip = 5000  # pula o começo para não pegar imagens já usadas no download inicial
    idx = 0
    replaced = 0
    for row in ds:
        if not need:
            break
        idx += 1
        if idx < skip:
            continue
        if row.get("labels") != 1:  # 1 = dog
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

    remaining = find_empty_labels()
    if remaining:
        print(f"Ainda vazias: {len(remaining)}")
        for p, _, _ in remaining:
            print(f"  {p.relative_to(ROOT)}")
    else:
        print("Todos os labels agora estão preenchidos.")


if __name__ == "__main__":
    main()

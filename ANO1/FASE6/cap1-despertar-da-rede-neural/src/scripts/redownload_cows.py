"""Download 40 real cow images from COCO 2017 val split via HuggingFace (streaming).

COCO category id 21 = 'cow'. We stream the validation split, keep only images whose
annotations include at least one cow instance, and save them until we have 40.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from datasets import load_dataset
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FINAL = ROOT / "raw_downloads" / "cow"

TARGET = 40
MIN_SIZE = 300
# detection-datasets/coco uses zero-indexed 80-class taxonomy where cow = 19
COCO_COW_CATEGORY_ID = 19


def save(img: Image.Image, path: Path) -> None:
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(path, "JPEG", quality=92)


def main() -> None:
    # limpa pasta alvo
    if FINAL.exists():
        shutil.rmtree(FINAL)
    FINAL.mkdir(parents=True, exist_ok=True)

    print("Abrindo COCO val (streaming) via HF detection-datasets/coco...")
    ds = load_dataset("detection-datasets/coco", split="val", streaming=True)

    kept = 0
    scanned = 0
    for row in ds:
        scanned += 1
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
        raise SystemExit(f"ERRO: só consegui {kept}/{TARGET}.")


if __name__ == "__main__":
    main()

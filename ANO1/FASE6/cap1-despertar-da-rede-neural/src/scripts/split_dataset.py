"""Copy 40 cow + 40 dog raw images into dataset/{train,val,test}/images with a 32/4/4 split per class.

Deterministic: shuffled with a fixed seed so the split is reproducible across machines.
Idempotent: clears existing images in the destination folders before copying.
"""
from __future__ import annotations

import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw_downloads"
DATASET = ROOT / "dataset"

CLASSES = ["cow", "dog"]
SPLITS = {"train": 32, "val": 4, "test": 4}
SEED = 42


def clean_images(split: str) -> None:
    target = DATASET / split / "images"
    for p in target.glob("*"):
        if p.is_file():
            p.unlink()


def split_class(class_name: str) -> None:
    src_dir = RAW / class_name
    images = sorted(src_dir.glob("*.jpg"))
    total_required = sum(SPLITS.values())
    if len(images) < total_required:
        raise RuntimeError(
            f"Classe {class_name}: encontradas {len(images)} imagens, "
            f"precisamos de {total_required} (32+4+4)."
        )

    rng = random.Random(SEED)
    shuffled = images.copy()
    rng.shuffle(shuffled)

    cursor = 0
    for split, count in SPLITS.items():
        chosen = shuffled[cursor : cursor + count]
        cursor += count
        dst_dir = DATASET / split / "images"
        dst_dir.mkdir(parents=True, exist_ok=True)
        for img in chosen:
            shutil.copy2(img, dst_dir / img.name)
        print(f"  {class_name} -> {split}: {len(chosen)} imagens")


def main() -> None:
    for split in SPLITS:
        clean_images(split)
    for cls in CLASSES:
        split_class(cls)
    print("\nSplit concluído. Contagem final:")
    for split in SPLITS:
        n = len(list((DATASET / split / "images").glob("*.jpg")))
        print(f"  {split}: {n} imagens")


if __name__ == "__main__":
    main()

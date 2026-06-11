"""Copy 40 cow + 40 dog raw images into dataset/{train,val,test}/images with a 32/4/4 split per class.

Segunda etapa do pipeline. Pega o pool bruto em raw_downloads/ e distribui em três
splits no formato que o YOLOv5 espera:
  dataset/train/images/   (32 cow + 32 dog = 64)
  dataset/val/images/     ( 4 cow +  4 dog =  8)
  dataset/test/images/    ( 4 cow +  4 dog =  8)
                                       total = 80 imagens

Decisões de design:
- **Determinístico**: usamos `seed=42` no Random local (não no `random` global) para que
  qualquer pessoa que rodar o script tenha exatamente o mesmo split, em qualquer máquina.
- **Idempotente**: limpamos os destinos antes de copiar, então rodar 2x dá o mesmo resultado.
- **shutil.copy2**: copia preservando metadados (mtime), o que ajuda a auditoria.
- Os labels (.txt YOLO) são gerados depois, por auto_label.py — aqui só lidamos com imagens.
"""
from __future__ import annotations

import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw_downloads"
DATASET = ROOT / "dataset"

CLASSES = ["cow", "dog"]
# Mapeamento split -> quantidade por classe. Soma == 40 (total disponível por classe).
SPLITS = {"train": 32, "val": 4, "test": 4}
SEED = 42  # fixa o embaralhamento — qualquer alteração quebra a reprodutibilidade


def clean_images(split: str) -> None:
    """Remove imagens antigas do split antes de copiar as novas (idempotência)."""
    target = DATASET / split / "images"
    for p in target.glob("*"):
        if p.is_file():
            p.unlink()


def split_class(class_name: str) -> None:
    """Embaralha as 40 imagens da classe e distribui 32/4/4 nos três splits."""
    src_dir = RAW / class_name
    images = sorted(src_dir.glob("*.jpg"))  # sorted() garante ordem estável antes do shuffle
    total_required = sum(SPLITS.values())
    if len(images) < total_required:
        # Falha cedo se o pool bruto está incompleto — evita split silenciosamente errado.
        raise RuntimeError(
            f"Classe {class_name}: encontradas {len(images)} imagens, "
            f"precisamos de {total_required} (32+4+4)."
        )

    # Random local com seed fixa: NÃO usamos random.shuffle global pra não interferir com
    # outras chamadas a `random` no processo (boa prática em scripts reprodutíveis).
    rng = random.Random(SEED)
    shuffled = images.copy()
    rng.shuffle(shuffled)

    # Cursor avança pelos splits na ordem do dict (Python 3.7+ preserva ordem de inserção).
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
    # Auditoria final: contagem por split para detectar qualquer perda na cópia.
    print("\nSplit concluído. Contagem final:")
    for split in SPLITS:
        n = len(list((DATASET / split / "images").glob("*.jpg")))
        print(f"  {split}: {n} imagens")


if __name__ == "__main__":
    main()

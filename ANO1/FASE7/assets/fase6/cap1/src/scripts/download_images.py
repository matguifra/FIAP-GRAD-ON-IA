"""Download 40 dog + 40 cow images from public HuggingFace datasets.

Primeira etapa do pipeline: alimentar `raw_downloads/` com 40 imagens por classe a partir
de datasets públicos do HuggingFace, sem qualquer intervenção manual. Esse pool bruto é
depois consumido por split_dataset.py (que faz o split 32/4/4 reprodutível).

Observação importante: este script foi a primeira tentativa de baixar vacas (via
Francesco/animals-ij5d2). Na prática descobrimos que esse dataset retorna animais
variados e poucas vacas reais, então acabamos usando redownload_cows.py (COCO via HF) como
fonte definitiva. Mantivemos este aqui para histórico do pipeline.
"""
from pathlib import Path
from datasets import load_dataset
from PIL import Image

# Diretório onde o pool bruto é salvo. As subpastas cow/ e dog/ são criadas se não existirem.
BASE = Path("/Users/rivandoneto/fase6-yolo/raw_downloads")
(BASE / "dog").mkdir(parents=True, exist_ok=True)
(BASE / "cow").mkdir(parents=True, exist_ok=True)

N = 40              # quantas imagens queremos por classe (32 train + 4 val + 4 test)
MIN_SIZE = 300      # imagens muito pequenas ficam ruins no YOLO @ 640 — descartamos

def save(img, path):
    """Garante que a imagem é salva como JPEG RGB (YOLOv5 espera 3 canais)."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(path, "JPEG", quality=92)

def grab_dogs():
    """Baixa 40 cachorros do dataset microsoft/cats_vs_dogs.

    Esse dataset rotula cada imagem com `labels = 0` (gato) ou `labels = 1` (cachorro).
    Usamos streaming=True para não baixar o dataset inteiro (~25k imagens) — apenas
    iteramos até atingir N=40 cachorros válidos.
    """
    print("Baixando cachorros (microsoft/cats_vs_dogs)...")
    ds = load_dataset("microsoft/cats_vs_dogs", split="train", streaming=True, trust_remote_code=True)
    count = 0
    for row in ds:
        if count >= N:
            break
        if row.get("labels") != 1:  # 1 = dog, 0 = cat
            continue
        img = row["image"]
        if img.width < MIN_SIZE or img.height < MIN_SIZE:
            continue
        save(img, BASE / "dog" / f"dog_{count:03d}.jpg")
        count += 1
        if count % 10 == 0:
            print(f"  {count}/{N}")
    print(f"Cachorros salvos: {count}")

def grab_cows():
    """Tentativa inicial de baixar vacas via Francesco/animals-ij5d2.

    Esse dataset roboflow-style mistura várias espécies — sem filtro confiável por classe
    nesse formato, acabamos pegando animais que não eram vacas. Por isso o pipeline final
    usa redownload_cows.py (que filtra por categoria COCO=19 = cow). Mantemos aqui para
    referência histórica.
    """
    print("Baixando vacas (Francesco/animals-ij5d2)...")
    for ds_name in ["Francesco/animals-ij5d2"]:
        try:
            ds = load_dataset(ds_name, split="train", streaming=True)
            count = 0
            for row in ds:
                if count >= N:
                    break
                cats = row.get("objects", {}).get("category", [])
                if not cats:
                    continue
                # categorias vêm como int aqui; o filtro fino fica para o redownload_cows.
                img = row["image"]
                if img.width < MIN_SIZE or img.height < MIN_SIZE:
                    continue
                save(img, BASE / "cow" / f"cow_{count:03d}.jpg")
                count += 1
                if count % 10 == 0:
                    print(f"  {count}/{N}")
            print(f"Vacas salvas: {count}")
            return
        except Exception as e:
            print(f"Falha em {ds_name}: {e}")

if __name__ == "__main__":
    grab_dogs()
    grab_cows()
    print("\nImagens em:", BASE)

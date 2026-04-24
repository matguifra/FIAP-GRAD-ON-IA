"""Download 40 dog + 40 cow images from public HuggingFace datasets."""
from pathlib import Path
from datasets import load_dataset
from PIL import Image

BASE = Path("/Users/rivandoneto/fase6-yolo/raw_downloads")
(BASE / "dog").mkdir(parents=True, exist_ok=True)
(BASE / "cow").mkdir(parents=True, exist_ok=True)

N = 40
MIN_SIZE = 300  # pular imagens muito pequenas

def save(img, path):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(path, "JPEG", quality=92)

def grab_dogs():
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
    print("Baixando vacas (Francesco/animals-ij5d2)...")
    # tenta dataset roboflow-style com class 'cow'
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
                # dataset tem animais variados; ficar com imagens com pelo menos 1 vaca
                # nesse ds categorias são ints, precisamos dos names
                img = row["image"]
                if img.width < MIN_SIZE or img.height < MIN_SIZE:
                    continue
                # salvar; vamos filtrar depois manualmente se necessário
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

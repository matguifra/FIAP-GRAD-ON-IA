"""Generate YOLO-format labels for every image in dataset/{train,val,test}/images.

Terceira etapa do pipeline — rotulação automática usando um YOLOv5s pré-treinado em COCO.
Como COCO já tem as classes 'cow' (id 19 no modelo) e 'dog' (id 16), conseguimos pseudo-
labels de alta qualidade sem rotular manualmente nenhuma imagem.

REMAPEAMENTO DE CLASSES:
COCO usa cow=19 e dog=16. Nosso `data.yaml` define cow=0 e dog=1 (só duas classes, o
modelo vai treinar do zero a cabeça final). Esse remapeamento é feito no dicionário
`COCO_TO_OURS` e aplicado a cada detecção antes de escrever o label.

FORMATO YOLO (idêntico ao que o Make Sense IA exporta):
    <class_id> <x_center> <y_center> <width> <height>
todos normalizados para [0,1] em relação às dimensões da imagem. Uma linha por bbox.

Imagens sem detecção recebem um .txt VAZIO mesmo assim — o YOLOv5 reclama se o label
está faltando, mas aceita label vazio (interpreta como "imagem sem objeto"). As imagens
sem detecção são depois reprocessadas por fill_missing_labels.py (modelo maior @ 1280)
e, se ainda falharem, substituídas por replace_bad_images.py.
"""
from __future__ import annotations

from pathlib import Path

import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"

SPLITS = ["train", "val", "test"]

# IDs COCO -> nossos IDs. Esses dois números (19 e 16) são fixos na taxonomia COCO 80-classes.
COCO_COW_ID = 19
COCO_DOG_ID = 16
COCO_TO_OURS = {COCO_COW_ID: 0, COCO_DOG_ID: 1}

# Threshold permissivo (0.15) porque queremos aproveitar o máximo de detecções; o filtro
# semântico (a classe esperada bate com o nome do arquivo?) cuida dos falsos positivos.
CONF_THRESHOLD = 0.15
IOU_THRESHOLD = 0.45  # padrão do YOLOv5 para NMS (Non-Max Suppression)


def load_model():
    """Carrega YOLOv5s pré-treinado via torch.hub.

    O `trust_repo=True` evita o prompt interativo de "trust this code?". O hub baixa o
    repo ultralytics/yolov5 e o checkpoint yolov5s.pt na primeira execução (~14MB).
    """
    print("Carregando YOLOv5s pré-treinado (COCO)...")
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, trust_repo=True)
    model.conf = CONF_THRESHOLD
    model.iou = IOU_THRESHOLD
    # Restringe o detector a só dois IDs COCO — descarta detecções de outras 78 classes.
    model.classes = [COCO_COW_ID, COCO_DOG_ID]
    return model


def expected_class_from_name(image_path: Path) -> int:
    """Infere a classe esperada a partir do prefixo do nome do arquivo.

    Os arquivos do pool bruto são `cow_NNN.jpg` ou `dog_NNN.jpg` — então sabemos com
    certeza qual é a classe correta. Isso é usado para descartar detecções espúrias
    (ex: o modelo detecta um cachorro numa foto que era para ser de vaca).

    Retorna -1 se o nome não bate em nenhum dos prefixos (não acontece no nosso pipeline,
    mas é uma trava defensiva).
    """
    name = image_path.stem.lower()
    if name.startswith("cow"):
        return 0
    if name.startswith("dog"):
        return 1
    return -1


def label_split(split: str, model) -> tuple[int, int, int]:
    """Roda inferência em todas as imagens de um split e escreve os labels."""
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
            # size=640 é a resolução padrão do YOLOv5; a imagem é redimensionada
            # internamente mantendo proporção (letterbox).
            results = model(im, size=640)

        lines = []
        # results.xyxy[0] = tensor [N, 6] com (x1, y1, x2, y2, conf, class_id) por bbox.
        for *xyxy, conf, cls in results.xyxy[0].tolist():
            mapped = COCO_TO_OURS.get(int(cls))
            if mapped is None:
                continue  # classe COCO que não nos interessa
            # Filtro semântico: descarta bbox cuja classe não bate com o esperado.
            if expected_cls != -1 and mapped != expected_cls:
                continue
            # Conversão xyxy (cantos) -> xywh normalizado (centro + tamanho), formato YOLO.
            x1, y1, x2, y2 = xyxy
            xc = ((x1 + x2) / 2) / w
            yc = ((y1 + y2) / 2) / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
            lines.append(f"{mapped} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

        # Mesmo sem detecção, escrevemos um .txt vazio: YOLOv5 espera que cada imagem
        # tenha o seu label correspondente, ainda que vazio.
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

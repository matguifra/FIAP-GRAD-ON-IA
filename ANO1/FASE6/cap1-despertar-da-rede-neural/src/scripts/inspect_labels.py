"""Diagnostic: run YOLOv5s at low confidence on all raw images and report detected COCO classes per file.

Script de DIAGNÓSTICO (não faz parte do pipeline de produção). Foi usado durante o
desenvolvimento para validar se as imagens em raw_downloads/ realmente continham vacas
e cachorros, ou se algum dos datasets HF estava trazendo outros animais (foi assim que
detectamos que Francesco/animals-ij5d2 não servia para vacas, motivando a criação de
redownload_cows.py).

Roda YOLOv5s @ 640 com conf=0.10 (bem permissivo) e imprime, para cada classe esperada
(cow e dog), um contador de quais classes COCO o modelo realmente vê nas imagens.

Saída de exemplo:
    == cow (40 imagens) ==
    sem detecção: 1
    classes COCO detectadas (imagens contendo a classe):
      cow: 38
      person: 4
      sheep: 2

Se "cow" não fosse o mais comum nas fotos rotuladas como cow, o pool estaria contaminado.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw_downloads"


def main() -> None:
    # Modelo pequeno e rápido — não precisa de precisão alta para diagnóstico.
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, trust_repo=True)
    model.conf = 0.10  # permissivo: queremos ver TUDO que o modelo enxerga
    model.iou = 0.45
    # Note: NÃO restringimos `model.classes` aqui — queremos saber tudo que aparece.
    names = model.names  # dicionário {class_id: 'class_name'} das 80 classes COCO

    for class_name in ("cow", "dog"):
        imgs = sorted((RAW / class_name).glob("*.jpg"))
        # Counter: por imagem, contamos cada classe que aparece NO MÁXIMO 1 vez (set).
        # Assim o número reflete "em quantas imagens essa classe aparece", não o total
        # de bboxes (que seria enviesado por imagens com vários objetos).
        coco_counter: Counter[str] = Counter()
        no_det = 0
        for p in imgs:
            with Image.open(p) as im:
                res = model(im, size=640)
            detected = [names[int(c)] for *_, c in res.xyxy[0].tolist()]
            if not detected:
                no_det += 1
            else:
                coco_counter.update(set(detected))  # set() = uma contagem por imagem
        print(f"\n== {class_name} ({len(imgs)} imagens) ==")
        print(f"sem detecção: {no_det}")
        print("classes COCO detectadas (imagens contendo a classe):")
        # Top 15 evita poluir a saída com classes raras (1-2 ocorrências cada).
        for cls, n in coco_counter.most_common(15):
            print(f"  {cls}: {n}")


if __name__ == "__main__":
    main()

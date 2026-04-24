# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Visão Computacional com YOLOv5 — FarmTech Solutions (Fase 6, Cap. 1)

## Grupo FarmTech

## 👨‍🎓 Integrantes
- <a href="https://www.linkedin.com/in/rivando-neto/">Rivando Bezerra Cavalcanti Neto (RM568235)</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Leticia Angelim Guerra (RM567501)</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Tales Ferraz de Arruda Domienikan (RM567483)</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Matheus Guimarães França (RM567144)</a>
- <a href="https://www.linkedin.com/company/inova-fusca">João Rafael Gonçalves Ramos (RM567908)</a>

## 👩‍🏫 Professores
### Tutor(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Ana Cristina dos Santos</a>

---

## 📜 Descrição

A **FarmTech Solutions** está expandindo seu portfólio para **visão computacional**. Este projeto é uma prova de conceito end-to-end que demonstra como treinar um detector de objetos customizado — com a família **YOLOv5** — para distinguir duas classes bem diferentes no contexto do agronegócio: **`cow`** (vaca, objeto A) e **`dog`** (cachorro, objeto B).

O pipeline completo cobre:
1. **Coleta automatizada** de 80 imagens (40 por classe) a partir de datasets públicos no HuggingFace (`microsoft/cats_vs_dogs` para cachorros e `detection-datasets/coco` para vacas).
2. **Divisão determinística** 32/4/4 por classe (train/val/test) com `seed=42`.
3. **Rotulação automática** em formato YOLO (`<classe> <xc> <yc> <w> <h>` normalizado) usando YOLOv5s pré-treinado no COCO — o mesmo formato que o [Make Sense IA](https://www.makesense.ai) exporta.
4. **Cascata de fallback** para imagens difíceis: YOLOv5l @ 1280 → substituição de imagens que continuam sem detecção.
5. **Duas simulações de treino** com mesmas hiperparâmetros exceto número de épocas (30 vs. 60) para medir o ganho marginal.
6. **Avaliação comparativa** com `val.py` no split de teste e `detect.py` com bounding boxes nas 8 imagens nunca vistas.

O notebook principal é auto-contido e funciona tanto no **Google Colab** (montando o Google Drive) quanto em **ambiente local** (CPU ou GPU NVIDIA).

## 🎥 Vídeo demonstrativo (YouTube, não listado)

_adicionar link aqui antes da entrega_

## 📊 Resultados no conjunto de teste (8 imagens nunca vistas)

| run           | precision | recall | mAP@0.5 | mAP@0.5:0.95 |
| ------------- | --------- | ------ | ------- | ------------ |
| `cowdog_ep30` | 0.802     | 0.829  | 0.822   | 0.446        |
| `cowdog_ep60` | **0.854** | 0.781  | **0.824** | **0.581**  |

**Por classe (60 ep, test):** `cow` → mAP@0.5=0.654, mAP@0.5:0.95=0.434 · `dog` → mAP@0.5=0.995, mAP@0.5:0.95=0.727.

Leitura rápida:
- **mAP@0.5 satura** (0.822 → 0.824): com transfer learning do COCO, 30 épocas já resolvem o "fácil" — a classe está certa.
- **mAP@0.5:0.95 sobe 30% relativo** (0.446 → 0.581): o modelo de 60 épocas acerta as bounding boxes com mais precisão, não só a categoria.
- **60 épocas troca recall por precisão** (0.802/0.829 → 0.854/0.781): o modelo fica mais conservador, o que reduz falso-positivo — desejável quando um alerta em campo é caro.
- **Detecção qualitativa (conf=0.25)**: com 30 épocas, `dog_015` ficou sem bbox visível; com 60 épocas, **todas as 8 imagens de teste** foram detectadas.
- **Gap cow vs. dog**: fotos de cachorro têm sujeito dominante + fundo simples; fotos de vaca têm múltiplas instâncias em paisagem aberta com oclusão — bbox fica mais difícil.

Gráficos e prints das inferências estão em [`docs/results/`](docs/results/).

## 📁 Estrutura de pastas

```
cap1-despertar-da-rede-neural/
├── assets/                     # imagens do README (logo FIAP)
├── data/
│   └── dataset/                # 80 imagens (32/4/4 por classe) + labels YOLO
│       ├── data.yaml
│       ├── train/{images,labels}/
│       ├── val/{images,labels}/
│       └── test/{images,labels}/
├── docs/
│   └── results/
│       ├── ep30/               # inferências + curvas + matriz de confusão (30 épocas)
│       └── ep60/               # idem (60 épocas)
├── src/
│   ├── notebook/
│   │   └── RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb   # notebook end-to-end
│   └── scripts/
│       ├── download_images.py        # download inicial de cachorros (HF cats_vs_dogs)
│       ├── redownload_cows.py        # download de vacas via HF detection-datasets/coco
│       ├── split_dataset.py          # split 32/4/4 determinístico (seed 42)
│       ├── auto_label.py             # labels YOLO via YOLOv5s pré-treinado COCO
│       ├── fill_missing_labels.py    # fallback com YOLOv5l @ 1280
│       ├── replace_bad_images.py     # troca imagens sem detecção
│       └── inspect_labels.py         # diagnóstico dos labels gerados
├── data_local.yaml             # config YOLO com caminho absoluto (treino local)
├── requirements.txt            # dependências Python
└── README.md
```

## 🔧 Como executar o código

### Pré-requisitos
- Python 3.10+ (testado em 3.12)
- Git
- (Opcional) Conta Google para rodar no Colab com GPU T4 gratuita

### Opção A — Google Colab (recomendado para quem não tem GPU)

1. Faça upload desta pasta inteira para `MyDrive/fase6-yolo/` no seu Google Drive.
2. Abra `src/notebook/RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb` no Colab.
3. Rode as células em ordem — a primeira célula monta o Drive, clona o YOLOv5 oficial e instala dependências.
4. Os dois treinos (30 e 60 épocas) usam GPU automaticamente quando disponível.

### Opção B — Local (CPU ou GPU NVIDIA)

```bash
git clone https://github.com/matguifra/FIAP-GRAD-ON-IA.git
cd FIAP-GRAD-ON-IA/ANO1/FASE6/cap1-despertar-da-rede-neural

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Clonar YOLOv5 ao lado do projeto (o notebook faz isso automaticamente)
git clone https://github.com/ultralytics/yolov5.git
pip install -r yolov5/requirements.txt

# Abrir o notebook
jupyter lab src/notebook/RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb
```

### Reconstruir o dataset do zero (opcional)

```bash
python src/scripts/download_images.py      # 40 cachorros
python src/scripts/redownload_cows.py      # 40 vacas (COCO via HF)
python src/scripts/split_dataset.py        # split 32/4/4
python src/scripts/auto_label.py           # labels iniciais
python src/scripts/fill_missing_labels.py  # fallback yolov5l@1280
python src/scripts/replace_bad_images.py   # troca imagens sem detecção
```

> **Equivalência com Make Sense IA:** o formato de label gerado é idêntico ao que o Make Sense exporta em *YOLO format*. Rotulação 100% manual pelo site funcionaria sem alteração no pipeline de treino.

## 🧪 Experimentos

Duas rodadas comparativas, mesma base (`yolov5s.pt`, `img=640`, `batch=8`), variando apenas o número de épocas:

| run           | épocas | pasta (dentro de `yolov5/runs/train/`)  |
| ------------- | ------ | --------------------------------------- |
| `cowdog_ep30` | 30     | `cowdog_ep30/`                          |
| `cowdog_ep60` | 60     | `cowdog_ep60/`                          |

O notebook carrega os `results.csv` de cada execução e gera:
- Tabela comparativa (precisão, recall, mAP@0.5, mAP@0.5:0.95, losses finais).
- Curvas de mAP@0.5 por época.
- Curvas de `train/box_loss` vs `val/box_loss` para diagnóstico de overfitting.
- Grade com as 8 imagens de teste anotadas pelo modelo de cada rodada.

## 📚 Licença dos dados

- **Cachorros:** `microsoft/cats_vs_dogs` (Microsoft Research, uso acadêmico).
- **Vacas:** COCO 2017 val split via `detection-datasets/coco` (Creative Commons Attribution 4.0).

## 🗃 Histórico de lançamentos

* 0.1.0 - 23/04/2026
    * Primeira versão: pipeline de dataset, treinos 30ep e 60ep, notebook com análise comparativa no split de teste.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

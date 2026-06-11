# Fase 6 - CAP1: Visão Computacional com YOLOv5

## FarmTech Solutions

## 👨‍🎓 Integrantes

- [Rivando Bezerra Cavalcanti Neto (RM568235)](https://www.linkedin.com/in/rivando-neto/)
- [Leticia Angelim Guerra (RM567501)](https://www.linkedin.com/in/leticiaguerra)
- [Tales Ferraz de Arruda Domienikan (RM567483)](http://linkedin.com/in/tales-domienikan-9446ba391/)
- [Matheus Guimarães França (RM567144)](https://www.linkedin.com/in/matheus-frança-7b9925405)
- [João Rafael Gonçalves Ramos (RM567908)](https://www.linkedin.com/company/inova-fusca)

## 👩‍🏫 Professores

### Tutor(a)

- [Ana Cristina dos Santos](https://www.linkedin.com/in/anacristinadossantos/)

### Coordenador(a)

- [André Godoi Chiovato](https://www.linkedin.com/in/andregodoichiovato/)

---

## 📜 Descrição

A **FarmTech Solutions** expandiu seu projeto para a área de **visão computacional**, desenvolvendo uma prova de conceito com **YOLOv5** para detecção de objetos no contexto do agronegócio.

A proposta foi treinar um modelo customizado capaz de identificar duas classes distintas:

- `cow` — vaca;
- `dog` — cachorro.

O projeto demonstra um pipeline completo de visão computacional, desde a coleta e organização das imagens até a rotulação, treinamento, avaliação e comparação dos resultados.

---

## 🎯 Objetivo

O objetivo principal foi aplicar técnicas de visão computacional para treinar um modelo de detecção de objetos com YOLOv5.

A atividade teve como objetivos:

- coletar imagens de datasets públicos;
- organizar imagens em treino, validação e teste;
- gerar labels no formato YOLO;
- treinar modelos com diferentes quantidades de épocas;
- avaliar os resultados com métricas de detecção;
- comparar o desempenho entre os treinamentos;
- gerar inferências visuais com bounding boxes;
- documentar o pipeline e os resultados.

---

## 🧠 Pipeline do Projeto

O pipeline desenvolvido cobre as seguintes etapas:

1. Coleta automatizada de imagens;
2. Separação em treino, validação e teste;
3. Rotulação automática em formato YOLO;
4. Uso de fallback para imagens com baixa detecção;
5. Treinamento com YOLOv5;
6. Comparação entre modelos de 30 e 60 épocas;
7. Avaliação no conjunto de teste;
8. Geração de inferências com bounding boxes.

---

## 🐄🐕 Classes Detectadas

| Classe | Descrição |
|---|---|
| `cow` | Vaca |
| `dog` | Cachorro |

O dataset foi organizado com imagens das duas classes, permitindo treinar o modelo para distinguir os objetos em diferentes contextos visuais.

---

## 📊 Dataset

Foram utilizadas **80 imagens**, divididas igualmente entre as duas classes:

| Classe | Total |
|---|---:|
| Cow | 40 |
| Dog | 40 |

A divisão foi feita de forma determinística com `seed=42`:

| Split | Quantidade por classe |
|---|---:|
| Treino | 32 |
| Validação | 4 |
| Teste | 4 |

Total do conjunto de teste: **8 imagens nunca vistas**.

---

## 🏷️ Rotulação

As imagens foram rotuladas no formato YOLO:

```text
<class_id> <x_center> <y_center> <width> <height>
```

Os valores são normalizados entre 0 e 1.

Esse formato é equivalente ao exportado por ferramentas como o **Make Sense IA**, permitindo compatibilidade com pipelines tradicionais de treinamento YOLO.

---

## 🤖 Modelo Utilizado

O projeto utiliza a família **YOLOv5** para detecção de objetos.

Foram realizadas duas simulações de treinamento:

| Run | Épocas |
|---|---:|
| `cowdog_ep30` | 30 |
| `cowdog_ep60` | 60 |

As duas rodadas usaram a mesma base e configurações semelhantes, variando principalmente o número de épocas.

---

## 📈 Resultados

### Resultados gerais no conjunto de teste

| Run | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---|---:|---:|---:|---:|
| `cowdog_ep30` | 0.802 | 0.829 | 0.822 | 0.446 |
| `cowdog_ep60` | 0.854 | 0.781 | 0.824 | 0.581 |

### Leitura dos resultados

O modelo de **60 épocas** apresentou melhor precisão e maior mAP@0.5:0.95, indicando bounding boxes mais ajustadas.

O modelo de **30 épocas** já apresentou bom desempenho em mAP@0.5, mostrando que o transfer learning com YOLOv5 conseguiu aprender rapidamente a diferença entre as classes.

A principal diferença entre os modelos está na qualidade da localização dos objetos, não apenas na identificação da classe.

---

## 🔎 Análise por Classe

No modelo de 60 épocas:

| Classe | mAP@0.5 | mAP@0.5:0.95 |
|---|---:|---:|
| Cow | 0.654 | 0.434 |
| Dog | 0.995 | 0.727 |

A classe `dog` apresentou desempenho superior, provavelmente por conter imagens com objetos mais centralizados e fundos mais simples.

A classe `cow` foi mais desafiadora por envolver múltiplas instâncias, paisagens abertas e possíveis oclusões.

---

## 🎥 Vídeo Demonstrativo

O vídeo demonstrativo do projeto está disponível em:

```text
https://youtu.be/nzV1QY16FQk
```

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal;
- **YOLOv5** — modelo de detecção de objetos;
- **PyTorch** — base para treinamento do modelo;
- **Google Colab** — ambiente recomendado para uso com GPU;
- **Jupyter Notebook** — desenvolvimento do pipeline;
- **HuggingFace Datasets** — origem de parte dos dados;
- **COCO Dataset** — origem das imagens de vacas;
- **Make Sense IA** — referência de formato para rotulação YOLO.

---

## 📁 Estrutura de Arquivos

```text
cap1/
├── README.md
├── requirements.txt
├── data_local.yaml
├── data/
│   └── dataset/
│       ├── data.yaml
│       ├── train/
│       │   ├── images/
│       │   └── labels/
│       ├── val/
│       │   ├── images/
│       │   └── labels/
│       └── test/
│           ├── images/
│           └── labels/
├── docs/
│   └── results/
│       ├── ep30/
│       └── ep60/
├── src/
│   ├── notebook/
│   │   └── RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb
│   └── scripts/
│       ├── download_images.py
│       ├── redownload_cows.py
│       ├── split_dataset.py
│       ├── auto_label.py
│       ├── fill_missing_labels.py
│       ├── replace_bad_images.py
│       └── inspect_labels.py
└── ir_alem/
```

---

## 🔧 Como Executar

### Pré-requisitos

- Python 3.10 ou superior;
- Git;
- Jupyter Notebook, JupyterLab, Google Colab ou VS Code com suporte a notebooks;
- GPU NVIDIA ou Google Colab com GPU para melhor desempenho.

---

### Opção 1: Google Colab

1. Faça upload da pasta do projeto para o Google Drive.

2. Abra o notebook:

```text
src/notebook/RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb
```

3. Execute as células em ordem.

4. O notebook instala dependências, prepara o ambiente e executa o pipeline de treinamento e avaliação.

---

### Opção 2: Execução Local

Acesse a pasta do CAP1:

```bash
cd assets/fase6/cap1
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Clone o YOLOv5:

```bash
git clone https://github.com/ultralytics/yolov5.git
pip install -r yolov5/requirements.txt
```

Abra o notebook:

```bash
jupyter lab src/notebook/RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb
```

---

## 🔁 Reconstrução do Dataset

Para reconstruir o dataset do zero, execute os scripts na sequência:

```bash
python src/scripts/download_images.py
python src/scripts/redownload_cows.py
python src/scripts/split_dataset.py
python src/scripts/auto_label.py
python src/scripts/fill_missing_labels.py
python src/scripts/replace_bad_images.py
```

Esses scripts baixam imagens, organizam os splits e geram labels compatíveis com YOLO.

---

## 🧪 Experimentos

As duas rodadas de treinamento foram:

| Run | Épocas | Pasta de saída |
|---|---:|---|
| `cowdog_ep30` | 30 | `cowdog_ep30/` |
| `cowdog_ep60` | 60 | `cowdog_ep60/` |

O notebook gera:

- tabela comparativa de métricas;
- curvas de desempenho;
- análise de perdas;
- matriz de confusão;
- inferências visuais com bounding boxes.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo da proposta;
- descrição das classes;
- estrutura do dataset;
- resultados dos modelos;
- notebook do projeto;
- arquivos de configuração;
- scripts auxiliares;
- imagens e evidências;
- documentação do CAP1.

Essa integração centraliza a entrega de visão computacional junto às demais fases do projeto.

---

## ✅ Status

| Item | Status |
|---|---|
| Dataset organizado | ✅ Concluído |
| Labels YOLO | ✅ Gerados |
| Treino 30 épocas | ✅ Concluído |
| Treino 60 épocas | ✅ Concluído |
| Avaliação dos modelos | ✅ Concluída |
| Inferências visuais | ✅ Geradas |
| Notebook | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📚 Licença dos Dados

- **Cachorros:** `microsoft/cats_vs_dogs`, Microsoft Research, uso acadêmico;
- **Vacas:** COCO 2017 val split via `detection-datasets/coco`, Creative Commons Attribution 4.0.

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="../../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

# 🚀 FASE 6 — Visão Computacional e Redes Neurais

## 📚 Graduação ON em Inteligência Artificial

## 👩🏻‍💻 Sobre esta Fase

Esta fase representa uma etapa da minha evolução na Graduação ON em Inteligência Artificial da FIAP.

Aqui estão organizados:

- 📖 Conteúdos teóricos estudados
- 🧠 Conceitos fundamentais consolidados
- 🛠 Tecnologias aplicadas
- 📂 Projetos desenvolvidos
- 📊 Resultados obtidos
- 🎯 Competências adquiridas

Esta documentação tem como objetivo demonstrar, de forma estruturada, o que foi aprendido e aplicado durante esta etapa do curso.

---

## 👥 Integrantes

| Nome | RM |
|---|---|
| Tales Ferraz de Arruda Domienikan | RM567483 |
| Leticia Angelim Guerra | RM567501 |
| Rivando Bezerra Cavalcanti Neto | RM568235 |
| Matheus Guimarães França | RM567144 |
| João Rafael Gonçalves Ramos | RM567908 |

---

## 🎯 Objetivo da Fase

Aplicar conceitos de Deep Learning e Visão Computacional na construção de modelos de detecção de objetos aplicados ao agronegócio, com foco em:

- Compreender os fundamentos de Redes Neurais e Deep Learning
- Construir pipelines completos de Visão Computacional (coleta → rotulação → treino → avaliação)
- Aplicar transfer learning com modelos pré-treinados (YOLOv5)
- Realizar experimentos comparativos variando hiperparâmetros
- Avaliar modelos por meio de métricas de detecção de objetos

## 📖 Conteúdos Abordados

- Fundamentos de Redes Neurais e Deep Learning
- Visão Computacional aplicada à detecção de objetos
- Arquitetura YOLO (You Only Look Once)
- Transfer learning com modelos pré-treinados no COCO
- Construção e rotulação de datasets customizados (formato YOLO)
- Métricas de avaliação: precision, recall, mAP@0.5 e mAP@0.5:0.95
- Análise comparativa de hiperparâmetros (número de épocas)
- Diagnóstico de overfitting com curvas de loss

## 🛠 Tecnologias Utilizadas

Durante esta fase, foram utilizadas as seguintes tecnologias:

- Python 3.10+
- YOLOv5 (Ultralytics)
- PyTorch
- HuggingFace Datasets (`microsoft/cats_vs_dogs`, `detection-datasets/coco`)
- Jupyter Notebook / Google Colab
- Git

## 📂 Projetos Desenvolvidos

### 📌 Projeto 1 — FarmTech Solutions: Visão Computacional com YOLOv5

**Descrição:**
Prova de conceito end-to-end de Visão Computacional para a FarmTech Solutions, com o objetivo de treinar um detector de objetos customizado capaz de distinguir duas classes no contexto do agronegócio: `cow` (vaca) e `dog` (cachorro). O projeto cobre todo o pipeline — desde a coleta automatizada de 80 imagens em datasets públicos (HuggingFace), passando pela rotulação automática em formato YOLO, até o treinamento de duas rodadas (30 e 60 épocas) com avaliação comparativa de métricas e bounding boxes.

**Tecnologias utilizadas:**

- Python 3.10+
- YOLOv5 (modelos `yolov5s` e `yolov5l`)
- PyTorch
- HuggingFace Datasets
- Google Colab (GPU T4) / Jupyter Notebook
- Git

**Principais aprendizados:**

- Construção de um pipeline completo de Visão Computacional (coleta → split → rotulação → treino → avaliação)
- Aplicação de transfer learning a partir de modelos pré-treinados no COCO
- Análise comparativa de modelos variando o número de épocas (30 vs 60)
- Interpretação de métricas de detecção (precision, recall, mAP@0.5 e mAP@0.5:0.95)
- Diagnóstico de trade-off entre precisão e recall em problemas reais
- Uso de cascata de fallback para tratar imagens difíceis durante a rotulação automática

## 🧠 Competências Desenvolvidas

Ao final desta fase, consolidei:

- ✔️ Capacidade de estruturar problemas de Visão Computacional aplicados ao agronegócio
- ✔️ Construção e avaliação de modelos de detecção de objetos
- ✔️ Aplicação de transfer learning com redes pré-treinadas
- ✔️ Construção e rotulação de datasets customizados em formato YOLO
- ✔️ Análise crítica de métricas de detecção e diagnóstico de overfitting
- ✔️ Documentação técnica clara
- ✔️ Versionamento e organização de código
- ✔️ Comunicação técnica de soluções

## 📋 Licença

Este projeto acadêmico segue o modelo de documentação FIAP.

MODELO GIT FIAP por FIAP está licenciado sob Attribution 4.0 International.

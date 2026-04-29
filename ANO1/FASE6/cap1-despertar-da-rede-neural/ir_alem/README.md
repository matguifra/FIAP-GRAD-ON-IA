# 🚀 Projeto Ir Além: Classificação com Transfer Learning e Segmentação  
### 📌 Fase 6 – Capítulo 1 | Opção 3.2  

---

## 📜 Descrição

Este projeto corresponde à atividade **“Ir Além” da Fase 6 – Capítulo 1**, na qual foi escolhida a opção **3.2) Transfer Learning e Fine Tuning**.

Foi desenvolvida uma abordagem de **classificação de imagens** utilizando o dataset criado na etapa principal (classes *cow* e *dog*).

O objetivo foi investigar duas hipóteses principais:

- Redes pré-treinadas (Transfer Learning) apresentam melhor desempenho do que redes treinadas do zero?  
- A remoção do fundo das imagens (segmentação) melhora a capacidade de classificação do modelo?  

Para isso, foram combinadas técnicas de **Transfer Learning**, **Fine Tuning** e **segmentação automática de imagens**.

---

## 🛠️ Tecnologias e Arquitetura

- **Modelo Base:** MobileNetV2 (pré-treinada na ImageNet)  
- **Framework:** TensorFlow / Keras  
- **Técnicas:** Transfer Learning e Fine Tuning  
- **Segmentação:** Biblioteca `rembg` (baseada no modelo U2-Net)  

---

## ⚙️ Fluxo de Processamento (Arquitetura do Projeto)

```text
Entrada: Imagens originais (cow / dog)
↓
Segmentação: Remoção automática do fundo (rembg)
↓
Transfer Learning: Extração de características (MobileNetV2 congelada)
↓
Fine Tuning: Ajuste das últimas camadas
↓
Saída: Classificação binária (cow vs dog)
```
## 🧠 Justificativa das Escolhas Técnicas

### 1) Por que MobileNetV2?

A MobileNetV2 foi escolhida por oferecer um bom equilíbrio entre desempenho e eficiência computacional.

Por ser treinada na ImageNet (mais de 1 milhão de imagens), a rede já possui filtros capazes de identificar:

- texturas  
- bordas  
- formas complexas  

Isso é especialmente importante em um cenário com apenas 80 imagens, onde o treinamento do zero seria limitado.

---

### 2) Estratégia de Fine Tuning

A estratégia adotada foi dividida em duas etapas:

- **Congelamento inicial:** todas as camadas da MobileNetV2 foram congeladas, treinando apenas a camada final de classificação  
- **Fine Tuning:** as últimas 20 camadas foram descongeladas com uma taxa de aprendizado reduzida (`1e-5`)  

Essa abordagem permitiu:

- preservar o conhecimento prévio da ImageNet  
- adaptar o modelo para características específicas de vacas e cachorros  
- reduzir o risco de overfitting com poucos dados  

---

## 🧪 Experimento de Segmentação (Remoção de Fundo)

Uma das hipóteses avaliadas foi:

**A remoção do fundo melhora a classificação das imagens?**

### 🔬 Metodologia

- Aplicação de segmentação automática utilizando a biblioteca `rembg`  
- Criação de um novo dataset contendo apenas os objetos principais  
- Treinamento do modelo com as imagens segmentadas  
- Comparação dos resultados com o modelo treinado com imagens originais  

Essa abordagem teve como objetivo reduzir ruídos visuais e direcionar o modelo para as características mais relevantes dos objetos.

---

## 📊 Resultados

- O modelo com Transfer Learning apresentou **alto desempenho**  
- A remoção de fundo **não trouxe melhoria significativa na acurácia**  
- O modelo já conseguia identificar corretamente os objetos mesmo com o fundo  

 **Observação:**  
O conjunto de teste contém apenas **8 imagens**, o que pode limitar a generalização dos resultados.

---

## 🖼️ Análise da Segmentação

- Em imagens com um único objeto → resultado satisfatório  
- Em imagens com múltiplos objetos → todos os elementos do primeiro plano foram mantidos  

Isso indica que a técnica:

- não distingue semanticamente os objetos  
- apenas separa fundo e primeiro plano  

## 🎬 Demonstração

- 📓 Notebook : [abrir notebook](https://github.com/matguifra/FIAP-GRAD-ON-IA/blob/main/ANO1/FASE6/cap1-despertar-da-rede-neural/ir_alem/LeticiaAngelimGuerra_rm567501_pbl_fase6_ir_alem.ipynb)

- 🎥 Vídeo:  
[INSERIR LINK DO YOUTUBE]

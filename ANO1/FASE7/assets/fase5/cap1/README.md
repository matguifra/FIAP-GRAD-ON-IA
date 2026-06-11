# Fase 5 - CAP1: Previsão de Rendimento de Safra com Machine Learning e AWS

## FarmTech Solutions

**Curso:** IA - FIAP  
**Fase:** 5  
**Grupo:** 8  
**Turma:** 1TIAOR

---

## 👨‍🎓 Integrantes

| Nome | RM |
|---|---|
| João Rafael Gonçalves Ramos | RM567908 |
| Letícia Angelim Guerra | RM567501 |
| Matheus Guimarães França | RM567144 |
| Rivando Bezerra Cavalcanti Neto | RM568235 |
| Tales Ferraz de Arruda Domienikan | RM567483 |

---

## 📜 Descrição

Este projeto foi desenvolvido para a **FarmTech Solutions**, empresa voltada à aplicação de Inteligência Artificial no agronegócio.

A proposta consiste em analisar uma base de dados agrícolas e climáticos para prever o **rendimento de safra** de diferentes culturas. Além da etapa de Machine Learning, a atividade também inclui uma análise de custos em nuvem usando a **AWS Pricing Calculator**, considerando a hospedagem do modelo em uma API.

O projeto combina:

- análise exploratória de dados;
- clusterização;
- detecção de outliers;
- modelos supervisionados de regressão;
- comparação de métricas;
- estimativa de custo em AWS;
- documentação e evidências da entrega.

---

## 🎯 Objetivo

O objetivo principal foi construir uma solução capaz de apoiar a tomada de decisão agrícola por meio da previsão do rendimento de safra.

A atividade teve como objetivos:

- explorar uma base de dados com informações climáticas e agrícolas;
- identificar relações entre clima, cultura e rendimento;
- aplicar clusterização para encontrar padrões nos dados;
- detectar possíveis outliers;
- treinar cinco modelos de regressão supervisionada;
- comparar os modelos com métricas adequadas;
- estimar o custo de infraestrutura em nuvem para hospedar o modelo;
- justificar a escolha da região AWS mais adequada.

---

## 🌾 Dataset

O dataset utilizado foi:

```text
crop_yield.csv
```

A base contém **155 registros** relacionados a **4 culturas agrícolas**.

### Variáveis

| Variável | Descrição |
|---|---|
| `Crop` | Nome da cultura agrícola |
| `Precipitation (mm day-1)` | Precipitação em milímetros por dia |
| `Specific Humidity at 2 Meters (g/kg)` | Umidade específica a 2 metros do solo |
| `Relative Humidity at 2 Meters (%)` | Umidade relativa a 2 metros do solo |
| `Temperature at 2 Meters (C)` | Temperatura a 2 metros do solo |
| `Yield` | Rendimento em toneladas por hectare |

---

## 🧠 Etapas do Projeto

### 1. Análise Exploratória dos Dados

Nesta etapa, foram realizadas análises para compreender o comportamento das variáveis.

Foram explorados pontos como:

- estatísticas descritivas;
- distribuição das variáveis;
- comparação entre culturas;
- correlações;
- visualizações gráficas;
- possíveis padrões entre clima e rendimento.

### 2. Clusterização

A etapa de aprendizado não supervisionado foi usada para identificar agrupamentos dentro da base.

Foram aplicadas técnicas como:

- método do cotovelo;
- KMeans;
- visualização com PCA;
- análise de agrupamentos;
- detecção de possíveis outliers.

### 3. Modelagem Preditiva

Foram utilizados cinco modelos de regressão supervisionada para prever o rendimento das safras.

Modelos trabalhados:

- Regressão Linear;
- Ridge Regression;
- Lasso Regression;
- Random Forest Regressor;
- Gradient Boosting Regressor.

### 4. Comparação dos Modelos

Os modelos foram avaliados com métricas adequadas para regressão, como:

- R²;
- MAE;
- MSE;
- RMSE;
- validação cruzada.

Essa comparação permite identificar qual modelo apresenta melhor desempenho para previsão do rendimento agrícola.

---

## ☁️ Entrega 2 - Computação em Nuvem AWS

A segunda entrega analisou o custo de hospedar o modelo em nuvem para disponibilizá-lo por meio de uma API.

O serviço escolhido foi:

```text
Amazon EC2
```

A estimativa foi feita usando a **AWS Pricing Calculator**.

### Configuração considerada

| Parâmetro | Escolha | Motivo |
|---|---|---|
| Serviço | Amazon EC2 | Permite hospedar a API do modelo |
| Instância | t3a.micro | Baixo custo e recursos suficientes para o cenário |
| Sistema operacional | Linux | Conforme solicitado na atividade |
| Armazenamento | 50 GB EBS gp3 | Custo menor e boa performance |
| Modelo de cobrança | On-Demand | Conforme solicitado |
| Uso mensal | 730 horas | Execução contínua 24/7 |

---

## 💰 Comparação de Custos AWS

| Região | Código | Custo mensal estimado |
|---|---|---:|
| Virgínia do Norte | us-east-1 | US$ 10,86 |
| São Paulo | sa-east-1 | US$ 18,62 |

Apesar da região da Virgínia do Norte apresentar menor custo, a região de **São Paulo** foi escolhida por critérios técnicos e legais.

### Justificativas para São Paulo

- **LGPD:** manter os dados no Brasil reduz riscos legais relacionados ao tratamento de dados nacionais;
- **Latência:** sensores no Brasil tendem a se comunicar mais rapidamente com servidores no Brasil;
- **Soberania dos dados:** dados estratégicos de produção agrícola permanecem sob jurisdição nacional;
- **Operação em tempo real:** menor latência favorece aplicações conectadas a sensores e monitoramento agrícola.

---

## 🎥 Vídeos Demonstrativos

### Entrega 1 - Machine Learning

```text
https://youtu.be/rW4sRL_B4HM
```

### Entrega 2 - AWS

```text
https://youtu.be/Pp_OM9_DHxg
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal;
- **Pandas** — manipulação de dados;
- **NumPy** — operações numéricas;
- **Matplotlib** — visualização de dados;
- **Seaborn** — visualizações estatísticas;
- **Scikit-learn** — Machine Learning;
- **Jupyter Notebook** — desenvolvimento da análise;
- **AWS Pricing Calculator** — estimativa de custos em nuvem;
- **Amazon EC2** — serviço de computação em nuvem avaliado.

---

## 📁 Estrutura de Arquivos

```text
cap1/
├── README.md
├── crop_yield.csv
├── executed_notebook.ipynb
├── RivandoBezerra_rm568235_pbl_fase4.ipynb
├── ROTEIRO_VIDEO.md
├── ir_alem
└── ATV5_2/
    ├── 01-sp-instancia-t3a-micro-custo.png
    ├── 02-armazenamento-ebs-gp3-50gb.png
    ├── 03-virginia-instancia-t3a-micro-custo.png
    └── 04-comparacao-preco-final-sp-vs-virginia.png
```

---

## 🔧 Como Executar

### Pré-requisitos

- Python 3.8 ou superior;
- Jupyter Notebook, JupyterLab, Google Colab ou VS Code com suporte a notebooks.

Instale as dependências principais:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Executar o notebook

Acesse a pasta do CAP1:

```bash
cd assets/fase5/cap1
```

Abra o notebook:

```bash
jupyter notebook RivandoBezerra_rm568235_pbl_fase4.ipynb
```

ou:

```bash
jupyter notebook executed_notebook.ipynb
```

Execute as células em sequência para visualizar a análise, os modelos e os resultados.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo do projeto;
- dataset `crop_yield.csv`;
- notebooks da entrega;
- análise de custos AWS;
- prints da AWS Pricing Calculator;
- roteiro do vídeo;
- documentação do CAP1.

A Fase 5 também foi conectada ao módulo de **alertas AWS da Fase 7**, que usa AWS SNS para enviar notificações baseadas em dados de sensores agrícolas.

---

## ✅ Status

| Item | Status |
|---|---|
| Dataset `crop_yield.csv` | ✅ Disponível |
| Análise exploratória | ✅ Concluída |
| Clusterização | ✅ Concluída |
| Modelos de regressão | ✅ Concluídos |
| Comparação de métricas | ✅ Concluída |
| Estimativa de custos AWS | ✅ Concluída |
| Prints da AWS Pricing Calculator | ✅ Disponíveis |
| Vídeos demonstrativos | ✅ Disponíveis |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

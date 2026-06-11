# Fase 4 - CAP1: Estimador de Irrigação Agrícola

## FarmTech Solutions

## 👨‍🎓 Grupo 33

| Nome | RM | GitHub |
|---|---|---|
| João Rafael Gonçalves Ramos | RM567908 | joaorafa-ramos |
| Letícia Angelim Guerra | RM567501 | leticiaguerrasoares |
| Matheus Guimarães França | RM567144 | matguifra |
| Rivando Bezerra Cavalcanti Neto | RM568235 | RivandoNeto |
| Tales Ferraz de Arruda Domienikan | RM567483 | domienik |

---

## 📜 Descrição

Este projeto consiste em uma aplicação **Streamlit** para estimar a quantidade de irrigação necessária para diferentes culturas agrícolas com base em variáveis ambientais, climáticas e agrícolas.

A solução utiliza uma base de dados agrícola e técnicas de **Data Science** e **Machine Learning** para explorar os dados, treinar modelos preditivos e apresentar os resultados em uma interface interativa.

---

## 🎯 Objetivo

O objetivo principal do CAP1 da Fase 4 foi desenvolver uma aplicação capaz de apoiar a tomada de decisão no contexto agrícola, estimando a irrigação necessária com base em dados como:

- características da cultura;
- variáveis ambientais;
- dados climáticos;
- informações do solo;
- histórico de dados agrícolas.

A aplicação foi organizada em páginas para facilitar a navegação entre a apresentação do projeto, exploração dos dados e modelagem preditiva.

---

## 🔗 Links do Projeto

### Aplicação publicada

```text
https://estimador-irrigacao.streamlit.app/
```

### Vídeo - Exploração dos Dados

```text
https://youtu.be/tSrq-A56gAg
```

### Vídeo - Modelagem e Avaliação

```text
https://youtu.be/ggH5JufFH_M
```

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal;
- **Streamlit** — construção da aplicação web;
- **Pandas** — manipulação de dados;
- **NumPy** — operações numéricas;
- **Scikit-learn** — modelagem preditiva;
- **Plotly** — gráficos interativos;
- **Matplotlib** — visualizações gráficas;
- **Seaborn** — visualizações estatísticas.

---

## 📁 Estrutura de Arquivos

```text
cap1/
├── fase4_home.py          # Página inicial adaptada para a dashboard da Fase 7
├── fase4_exploracao.py    # Página de exploração dos dados
├── fase4_modelagem.py     # Página de modelagem e avaliação
├── utils.py               # Funções auxiliares para carregamento e tratamento dos dados
├── produtos_agricolas.csv # Dataset usado no projeto
└── README.md              # Documentação do CAP1
```

> Observação: no projeto original, as páginas podiam estar nomeadas como `Home.py`, `pages/1_Exploração.py` e `pages/2_Modelagem.py`. Para a integração na Fase 7, os arquivos foram adaptados para funcionar dentro da estrutura central da dashboard.

---

## 📊 Dataset

O arquivo utilizado no projeto é:

```text
produtos_agricolas.csv
```

Esse dataset contém informações agrícolas utilizadas para:

- exploração dos dados;
- visualização de padrões;
- treinamento de modelos;
- avaliação do desempenho preditivo;
- estimativa de irrigação necessária.

---

## 🧭 Páginas da Aplicação

### Home

Apresenta a introdução do projeto, objetivo da solução e contexto geral do estimador de irrigação.

### Exploração

Permite analisar os dados agrícolas por meio de gráficos, estatísticas e visualizações interativas.

### Modelagem

Apresenta o processo de treinamento, avaliação e uso do modelo preditivo para estimar a irrigação.

---

## 🔧 Como Executar

### Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install streamlit pandas numpy scikit-learn plotly matplotlib seaborn
```

### Execução do projeto original

Caso esteja executando apenas o projeto original da Fase 4, acesse a pasta do CAP1 e rode:

```bash
streamlit run Home.py
```

### Execução pela dashboard da Fase 7

Na versão integrada da Fase 7, execute o projeto pela raiz do repositório:

```bash
streamlit run app.py
```

Depois acesse:

```text
Fase 4 - Dashboard e Data Science > CAP1 - Dashboard Agrícola
```

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard integrada, é possível acessar:

- Home do projeto de irrigação;
- exploração dos dados;
- modelagem preditiva;
- dataset agrícola;
- funções auxiliares;
- documentação do CAP1.

Essa integração permite centralizar a entrega da Fase 4 junto às demais fases do projeto FarmTech.

---

## ✅ Status

| Item | Status |
|---|---|
| Aplicação Streamlit | ✅ Concluída |
| Exploração dos dados | ✅ Concluída |
| Modelagem preditiva | ✅ Concluída |
| Vídeos demonstrativos | ✅ Disponíveis |
| Dataset | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

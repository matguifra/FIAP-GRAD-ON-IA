# FIAP - Faculdade de Informática e Administração Paulista

# A Primeira Técnica de Aprendizado de Máquina

## 👨‍🎓 Integrantes

- [João Rafael Gonçalves Ramos (RM567908)](https://www.linkedin.com/company/inova-fusca)
- [Leticia Angelim Guerra (RM567501)](https://www.linkedin.com/in/leticiaguerra)
- [Matheus Guimarães França (RM567144)](https://www.linkedin.com/in/matheus-frança-7b9925405)
- [Rivando Bezerra Cavalcanti Neto (RM568235)](https://www.linkedin.com/in/rivando-neto/)
- [Tales Ferraz de Arruda Domienikan (RM567483)](http://linkedin.com/in/tales-domienikan-9446ba391/)

## 👩‍🏫 Professores

### Tutor(a)

- [Ana Cristina dos Santos](https://www.linkedin.com/in/anacristinadossantos/)

### Coordenador(a)

- [André Godoi Chiovato](https://www.linkedin.com/in/andregodoichiovato/)

---

## 📜 Descrição

Nesta atividade de Ciência de Dados e Machine Learning, foi utilizada uma base de dados com informações de **solo**, **clima** e **cultivos agrícolas**.

A base contém variáveis relacionadas a nutrientes do solo, condições climáticas e tipo de cultura recomendada. A partir desses dados, foi desenvolvida uma análise exploratória e foram criados modelos preditivos para recomendar o melhor produto agrícola a ser cultivado de acordo com as condições informadas.

---

## 🎯 Objetivo

O objetivo principal do CAP10 foi aplicar técnicas de **Aprendizado de Máquina supervisionado** para resolver um problema de classificação no contexto do agronegócio.

A atividade teve como objetivos:

- analisar uma base agrícola;
- compreender as variáveis de solo e clima;
- realizar análise exploratória e descritiva;
- gerar visualizações gráficas;
- comparar diferentes culturas agrícolas;
- treinar modelos de Machine Learning;
- avaliar a performance dos modelos;
- recomendar a cultura mais adequada para determinadas condições.

---

## 🌱 Dataset

O projeto utiliza a base:

```text
produtos_agricolas.csv
```

A base contém informações relacionadas a nutrientes do solo, clima e cultura recomendada.

### Variáveis

| Variável | Descrição |
|---|---|
| `N` | Quantidade de nitrogênio no solo |
| `P` | Quantidade de fósforo no solo |
| `K` | Quantidade de potássio no solo |
| `temperature` | Temperatura média da região |
| `humidity` | Umidade média do ar |
| `pH` | pH do solo |
| `rainfall` | Precipitação em milímetros |
| `label` | Tipo de cultura recomendada |

---

## 🧠 Etapas do Projeto

O projeto foi dividido em duas grandes etapas:

### 1. Análise Exploratória e Descritiva

Nesta etapa, foram realizadas análises para entender a distribuição das variáveis e identificar padrões relevantes.

Foram trabalhados pontos como:

- estatísticas descritivas;
- comparação entre culturas;
- visualizações gráficas;
- análise de relações entre nutrientes, clima e produto agrícola;
- identificação de perfis ideais de solo e clima.

### 2. Modelagem Preditiva

Após a análise dos dados, foram desenvolvidos e comparados modelos preditivos de classificação.

O objetivo dos modelos foi prever qual cultura agrícola é mais indicada com base nas características do solo e do clima.

A avaliação foi realizada com métricas adequadas ao problema de classificação.

---

## 🤖 Modelos de Machine Learning

A atividade solicitou o desenvolvimento de cinco modelos preditivos com algoritmos diferentes.

Exemplos de algoritmos usados ou indicados para esse tipo de problema:

- K-Nearest Neighbors;
- Support Vector Machine;
- Random Forest;
- Naive Bayes;
- Logistic Regression;
- Decision Tree.

Os modelos foram comparados para verificar qual apresentou melhor desempenho na recomendação da cultura agrícola.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal;
- **Jupyter Notebook** — desenvolvimento da análise;
- **Pandas** — manipulação de dados;
- **NumPy** — operações numéricas;
- **Matplotlib** — visualizações gráficas;
- **Seaborn** — visualizações estatísticas;
- **Scikit-learn** — treinamento e avaliação dos modelos;
- **Google Colab** — ambiente de execução em nuvem.

---

## 📁 Estrutura de Arquivos

```text
cap10/
├── aprendizado-de-maquina.ipynb   # Notebook com análise, gráficos e modelos
├── produtos_agricolas.csv         # Dataset agrícola usado no projeto
└── README.md                      # Documentação do CAP10
```

---

## 🔧 Como Executar

### Opção 1: Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com/).

2. Faça o upload do notebook:

```text
aprendizado-de-maquina.ipynb
```

3. Quando o notebook solicitar o dataset, envie o arquivo:

```text
produtos_agricolas.csv
```

4. Execute as células em sequência.

---

### Opção 2: Execução Local

#### Pré-requisitos

- Python 3 instalado;
- Jupyter Notebook ou JupyterLab instalado;
- Bibliotecas necessárias instaladas.

Instale as dependências principais com:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

#### Passo a passo

1. Clone este repositório.

2. Acesse a pasta do CAP10:

```bash
cd assets/fase3/cap10
```

3. Inicie o Jupyter Notebook:

```bash
jupyter notebook aprendizado-de-maquina.ipynb
```

4. Execute as células em sequência.

> Observação: caso o notebook tenha sido criado para execução no Google Colab usando `google.colab import files`, em execução local pode ser necessário substituir a célula de upload por leitura direta com Pandas:
>
> ```python
> import pandas as pd
> df = pd.read_csv("produtos_agricolas.csv")
> ```

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo da atividade;
- explicação das variáveis do dataset;
- notebook do projeto;
- documentação do CAP10.

Essa integração permite consultar a entrega de Machine Learning dentro da plataforma central do projeto.

---

## ✅ Status

| Item | Status |
|---|---|
| Dataset agrícola | ✅ Disponível |
| Análise exploratória | ✅ Concluída |
| Visualizações gráficas | ✅ Concluídas |
| Modelagem preditiva | ✅ Concluída |
| Notebook Jupyter | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

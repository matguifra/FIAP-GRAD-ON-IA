# FIAP - Faculdade de Informática e Administração Paulista

# Implementando Algoritmos de Machine Learning com Scikit-learn

## Fase 4 - CAP3: Classificação de Sementes

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

Este projeto apresenta uma aplicação de **Machine Learning** para classificação inteligente de variedades de grãos de trigo.

A atividade utiliza o **Seeds Dataset**, disponível no UCI Machine Learning Repository, e aplica a metodologia **CRISP-DM** para organizar as etapas de entendimento do problema, análise dos dados, preparação, modelagem, avaliação e interpretação dos resultados.

O objetivo é automatizar a classificação de grãos, uma tarefa que em cooperativas agrícolas pequenas pode ser feita manualmente por especialistas, tornando o processo mais demorado e sujeito a erros humanos.

---

## 🎯 Objetivo

O objetivo principal do CAP3 foi desenvolver modelos de Machine Learning capazes de classificar variedades de grãos de trigo com base em suas características físicas.

O projeto contempla:

- análise exploratória dos dados;
- pré-processamento;
- identificação de relações entre variáveis;
- normalização ou padronização das características;
- treinamento de diferentes modelos de classificação;
- comparação de desempenho;
- otimização de modelos;
- interpretação dos resultados.

---

## 🌾 Dataset

O projeto utiliza o **Seeds Dataset**, composto por amostras de grãos de trigo pertencentes a três variedades:

- **Kama**
- **Rosa**
- **Canadian**

### Atributos do dataset

| Atributo | Descrição |
|---|---|
| Área | Medida da área do grão |
| Perímetro | Comprimento do contorno do grão |
| Compacidade | Relação entre área e perímetro |
| Comprimento do núcleo | Eixo principal do grão |
| Largura do núcleo | Eixo secundário do grão |
| Coeficiente de assimetria | Medida da assimetria do grão |
| Comprimento do sulco do núcleo | Comprimento do sulco central do grão |
| Classe | Variedade do trigo |

---

## 🧠 Etapas do Projeto

### 1. Análise e Pré-processamento

Nesta etapa, foram realizadas atividades como:

- carregamento do dataset;
- visualização das primeiras linhas;
- estatísticas descritivas;
- histogramas;
- boxplots;
- gráficos de dispersão;
- verificação de valores ausentes;
- análise da necessidade de escala das variáveis;
- aplicação de normalização ou padronização quando necessário.

---

### 2. Implementação dos Algoritmos

Foram testados diferentes algoritmos de classificação com a biblioteca **scikit-learn**.

Entre os algoritmos indicados ou utilizados estão:

- K-Nearest Neighbors;
- Support Vector Machine;
- Random Forest;
- Naive Bayes;
- Logistic Regression;
- Decision Tree.

Os dados foram separados em treino e teste para avaliar a capacidade de generalização dos modelos.

---

### 3. Avaliação dos Modelos

Os modelos foram avaliados com métricas adequadas para problemas de classificação, como:

- acurácia;
- precisão;
- recall;
- F1-score;
- matriz de confusão.

Essas métricas permitiram comparar os algoritmos e identificar quais apresentaram melhor desempenho para a classificação dos grãos.

---

### 4. Otimização

Quando necessário, foram exploradas configurações de hiperparâmetros para melhorar o desempenho dos modelos.

A otimização permite ajustar parâmetros dos algoritmos, buscando resultados mais consistentes e maior precisão na classificação.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal;
- **Jupyter Notebook** — desenvolvimento e documentação técnica;
- **Pandas** — manipulação de dados;
- **NumPy** — operações numéricas;
- **Matplotlib** — visualização de dados;
- **Seaborn** — visualizações estatísticas;
- **Scikit-learn** — treinamento e avaliação de modelos;
- **Google Colab** — opção de execução em nuvem.

---

## 📁 Estrutura de Arquivos

```text
cap3/
├── seeds_classification_ml.ipynb   # Notebook com análise, pré-processamento e modelos
├── seeds_dataset.txt               # Base de dados Seeds Dataset
└── README.md                       # Documentação do CAP3
```

---

## 🔧 Como Executar

### Opção 1: Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com/).

2. Faça upload do notebook:

```text
seeds_classification_ml.ipynb
```

3. Ao executar a célula de carregamento dos dados, envie o arquivo:

```text
seeds_dataset.txt
```

4. Execute as células em sequência até o final da análise e avaliação dos modelos.

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

1. Clone este repositório em sua máquina.

2. Acesse a pasta do CAP3:

```bash
cd assets/fase4/cap3
```

3. Inicie o Jupyter Notebook:

```bash
jupyter notebook seeds_classification_ml.ipynb
```

4. Execute as células em sequência.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo do CAP3;
- explicação do problema;
- descrição do dataset;
- etapas da metodologia CRISP-DM;
- notebook do projeto;
- documentação do CAP3.

Essa integração permite consultar a entrega de Machine Learning da Fase 4 dentro da plataforma final do projeto.

---

## ✅ Status

| Item | Status |
|---|---|
| Dataset Seeds | ✅ Disponível |
| Análise exploratória | ✅ Concluída |
| Pré-processamento | ✅ Concluído |
| Modelos de classificação | ✅ Concluídos |
| Avaliação dos modelos | ✅ Concluída |
| Notebook Jupyter | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

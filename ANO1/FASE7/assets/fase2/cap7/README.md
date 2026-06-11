# FIAP - Faculdade de Informática e Administração Paulista

# Decolando com Ciências de Dados - Agronegócio

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

O objetivo deste projeto foi aplicar conceitos fundamentais de **Ciência de Dados** no contexto do **agronegócio**.

A atividade solicitou a pesquisa de dados em fontes públicas brasileiras, como IBGE, CONAB, MAPA, Embrapa, INPE e CNA Brasil. A partir disso, foi criada uma base de dados estruturada em Excel com pelo menos 30 registros e variáveis de diferentes tipos:

- variável quantitativa discreta;
- variável quantitativa contínua;
- variável qualitativa nominal;
- variável qualitativa ordinal.

Depois da criação da base, foi desenvolvido um script em **R** para realizar uma análise exploratória dos dados, incluindo medidas estatísticas e visualizações gráficas.

---

## 🎯 Objetivo

O objetivo principal do CAP7 foi construir uma base de dados relacionada ao agronegócio e realizar uma análise estatística exploratória utilizando R.

A entrega contempla:

- criação de uma base em Excel;
- uso de variáveis quantitativas e qualitativas;
- análise de tendência central;
- análise de dispersão;
- cálculo de medidas separatrizes;
- gráficos para variáveis quantitativas;
- gráficos para variáveis qualitativas.

---

## 🛠️ Tecnologias Utilizadas

- **R** — análise estatística e geração de gráficos;
- **Excel** — estruturação da base de dados;
- **readxl** — leitura do arquivo Excel no R;
- **ggplot2** — criação de gráficos;
- **dplyr** — manipulação e organização dos dados.

---

## 📁 Estrutura de Arquivos

```text
cap7/
├── script_novo.R           # Script em R para análise exploratória dos dados
├── tabela_formatada.xlsx   # Base de dados estruturada em Excel
└── README.md               # Documentação do CAP7
```

---

## 📊 Base de Dados

O arquivo `tabela_formatada.xlsx` contém a base de dados usada na análise.

A base foi organizada para atender aos critérios da atividade, contendo variáveis dos seguintes tipos:

| Tipo de variável | Exemplo de uso |
|---|---|
| Quantitativa discreta | Quantidade, contagem ou número inteiro |
| Quantitativa contínua | Área, produção, valor ou medida numérica |
| Qualitativa nominal | Categoria sem ordem definida |
| Qualitativa ordinal | Categoria com ordem ou nível |

---

## 📈 Análise em R

O arquivo `script_novo.R` realiza a análise exploratória da base.

Entre as análises realizadas estão:

- leitura da base Excel;
- cálculo de média;
- cálculo de mediana;
- cálculo de desvio padrão;
- medidas de dispersão;
- medidas separatrizes;
- visualização gráfica de variável quantitativa;
- visualização gráfica de variável qualitativa.

---

## 🔧 Como Executar

### Pré-requisitos

É necessário ter o **R** instalado na máquina.

Também é necessário instalar os pacotes usados no script:

```r
install.packages(c("readxl", "ggplot2", "dplyr"))
```

### Passo a passo

1. Clone este repositório em sua máquina.

2. Acesse a pasta do CAP7:

```bash
cd assets/fase2/cap7
```

3. Execute o script em R:

```bash
Rscript script_novo.R
```

Caso execute pelo RStudio, configure o diretório de trabalho para a pasta onde estão o script e o arquivo Excel, garantindo que `tabela_formatada.xlsx` seja lido corretamente.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo da atividade;
- base de dados em Excel;
- estatísticas da base;
- código R;
- documentação do CAP7.

Essa integração permite consultar os materiais da análise diretamente pela aplicação Streamlit, mantendo os arquivos organizados dentro da estrutura final do projeto.

---

## ✅ Status

| Item | Status |
|---|---|
| Base Excel | ✅ Concluída |
| Script R | ✅ Concluído |
| Análise exploratória | ✅ Concluída |
| Gráficos estatísticos | ✅ Concluídos |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

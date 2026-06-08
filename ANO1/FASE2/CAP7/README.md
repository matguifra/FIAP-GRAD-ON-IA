# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
</a>
</p>

<br>

# Decolando com ciências de dados - Agronegócio

## 👨‍🎓 Integrantes

- <a href="https://www.linkedin.com/company/inova-fusca">João Rafael Gonçalves Ramos (RM567908)</a>
- <a href="https://www.linkedin.com/in/leticiaguerra">Leticia Angelim Guerra (RM567501)</a>
- <a href="https://www.linkedin.com/in/matheus-frança-7b9925405">Matheus Guimarães França (RM567144)</a>
- <a href="https://www.linkedin.com/in/rivando-neto/">Rivando Bezerra Cavalcanti Neto (RM568235)</a>
- <a href="http://linkedin.com/in/tales-domienikan-9446ba391/">Tales Ferraz de Arruda Domienikan (RM567483)</a>

## 👩‍🏫 Professores

### Tutor(a)

- <a href="https://www.linkedin.com/in/anacristinadossantos/">Ana Cristina dos Santos</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>

## 📜 Descrição

O objetivo deste projeto foi aplicar conceitos fundamentais de Ciência de Dados no contexto do agronegócio. Foi solicitado aos alunos pesquisar dados de fontes públicas brasileiras (como IBGE, CONAB, MAPA, etc.) e formar uma base de dados contendo pelo menos 30 instâncias e com tipos de variáveis específicos: qualitativas (nominal e ordinal) e quantitativas (discreta e contínua).

Após a elaboração da base, construímos um script na linguagem R que carrega os dados e realiza as respectivas análises exploratórias. Entre as análises efetuadas constam extrações de medidas de tendência central, medidas de dispersão e separatrizes para a variável quantitativa em destaque (Área Total). Também contemplamos a geração visual de distribuições numéricas e categóricas usando as bibliotecas padrão do R e a `ggplot2` para gráficos estéticos.

## 📁 Estrutura de pastas

- <b>script_novo.R</b>: Script desenvolvido em linguagem R focado em análise exploratória dos dados estatísticos, utilizando bibliotecas de tratamento numérico e plotagem de gráficos.
- <b>tabela_formatada.xlsx</b>: Base de dados estruturada em Excel contendo amostras da área do Agronegócio para ingestão e interpretação pelo script R.
- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Como executar

**Pré-requisitos:**

- [R](https://cran.r-project.org/) instalado na máquina.
- Instalar os seguintes pacotes do R, em sua primeira execução:
  - `readxl`
  - `ggplot2`
  - `dplyr`

**Passo a passo:**

1. Realize o clone deste repositório na sua máquina pessoal.
2. É fundamental certificar-se de ter instalado no RStudio ou R Console os pacotes necessários citados acimas. Para instalar, você pode rodar o comando `install.packages(c("readxl", "ggplot2", "dplyr"))` no console.
3. Acesse este diretório da entrega usando seu terminal ou linha de comando: `cd ANO1/FASE2/CAP7`
4. Na raiz da pasta, execute o script em linha de comando que aponta para nosso R:

   ```bash
   Rscript script_novo.R
   ```

   **Nota:** Se você for executar o script por dentro de uma IDE como RStudio, certifique-se de que a IDE define o diretório de trabalho "working directory" para o local deste script para que o arquivo `tabela_formatada.xlsx` seja lido com sucesso usando caminho relativo.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

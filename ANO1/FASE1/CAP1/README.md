# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
</a>
</p>

<br>

# Play na sua carreira em IA

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

A proposta deste trabalho, ambientado em uma startup fictícia chamada FarmTech Solutions, foi desenvolver uma aplicação em Python para auxiliar uma fazenda na migração para a Agricultura Digital. A solução implementada suporta dois tipos de culturas (soja e milho) e é responsável por calcular a área de plantio e a quantidade necessária de insumos e água para o manejo, baseando-se nas dimensões informadas pelo usuário e em dados da EMBRAPA. A aplicação possui um menu interativo que permite a entrada, consulta, atualização e remoção de dados das lavouras em vetores.

Na sequência, foi criado um script em R para calcular dados estatísticos básicos (como média, mediana e desvio padrão) com os dados gerados pela aplicação em Python.

## 📁 Estrutura de pastas

- <b>lavouras.py</b>: Script em Python desenvolvido para cálculos e gestão da lavoura.
- <b>lavouras.R</b>: Script em R desenvolvido para cálculos estatísticos.
- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Como executar o código

**Pré-requisitos:**

- Python 3 instalado
- R instalado

**Passo a passo:**

1. Clone este repositório em sua máquina.
2. Acesse a pasta do projeto pelo terminal: `cd ANO1/FASE1/CAP1`
3. Execute o script em Python:

   ```bash
   python lavouras.py
   ```

   Interaja com o menu no terminal para adicionar dados (escolha a cultura, informe a largura e comprimento). A opção `5` no próprio sistema te dará a string de saída que poderá ser ajustada dentro do código R.
4. Execute o script em R para ver as estatísticas (verifique no arquivo R os dados mockados no vetor):

   ```bash
   Rscript lavouras.R
   ```

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

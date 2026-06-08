# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
</a>
</p>

<br>

# Implementando Algoritmos de Machine Learning com Scikit-learn

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

O projeto abordou o desenvolvimento de uma aplicação de Inteligência Artificial para a classificação inteligente de grãos de trigo, com o uso da metodologia CRISP-DM. No contexto de automatizar uma tarefa muitas vezes manual e sujeita a erros, utilizamos características físicas dos grãos (como Área, Perímetro, Compactação e Largura/Comprimento do Núcleo) para treinar diferentes algoritmos em Python com a biblioteca **scikit-learn**.

Acompanhando os notebooks entregues, nós englobamos as seguintes etapas:

- **Análise e Pré-processamento**: onde visualizamos estatísticas das variáveis, lidamos com normalizações (usando `StandardScaler`) e buscamos outliers.
- **Implementação dos Algoritmos**: foram testados e criados modelos com abordagens distintas para prever a variedade correta do grão.
- **Otimização**: exploração das configurações de hiperparâmetros que extrairiam o máximo desempenho dos nossos classificadores.
- **Resultados**: avaliação documentada via matriz de confusão e métricas de acurácia, com conclusões que vinculam os resultados técnicos aos ganhos de negócio na agroindústria.

## 📁 Estrutura de pastas

- <b>seeds_classification_ml.ipynb</b>: O Jupyter Notebook que engloba totalmente os scripts de código utilizados, bem como a apresentação técnica completa desde o carregamento até a avaliação final dos modelos gerados.
- <b>seeds_dataset.txt</b>: Arquivo com a base de dados do Seeds Dataset original do repositório UCI.
- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Como executar o código

### Opção 1: Execução no Google Colab (Na nuvem)

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Faça o upload do arquivo `seeds_classification_ml.ipynb` presente nesta pasta.
3. Ao executar a célula referente à coleta de dados, o ambiente solicitará interativamente o upload do dataset. Selecione o arquivo `seeds_dataset.txt` que também está nesta pasta.
4. Continue executando as células sequencialmente até o final das etapas de ML e validação teórica.

### Opção 2: Execução Local (Em sua máquina)

**Pré-requisitos:**

- Ter o Python 3 instalado.
- Ter o Jupyter Notebook ou JupyterLab instalado.
- Instalar as dependências: `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn`.

**Passo a passo:**

1. Clone ou faça o download deste repositório para o seu computador.
2. Navegue até o diretório da atividade executando no terminal: `cd ANO1/FASE4/CAP3`.
3. Inicie sua plataforma Jupyter por meio do comando:

   ```bash
   jupyter notebook seeds_classification_ml.ipynb
   ```

4. Dentro do notebook, execute as células sequencialmente. O código detectará automaticamente o arquivo `seeds_dataset.txt` contido na mesma pasta e seguirá as análises sem pedir upload.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

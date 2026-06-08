# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
</a>
</p>

<br>

# A primeira técnica de aprendizado de máquina

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

Nesta atividade de Ciência de Dados e Machine Learning, trabalhamos com uma base de dados contendo informações detalhadas sobre condições de solo (Nitrogênio, Fósforo, Potássio e pH) e climáticas (temperatura, umidade e precipitação) correlacionadas a diferentes tipos de cultivos agrícolas.

O projeto foi dividido em suas principais fases:

1. **Análise Exploratória e Descritiva**: Para entender como essas variáveis se distribuem, detectar valores anômalos (se existissem) e tirar insights de negócio; gerando visualizações claras que explicam os cenários ideais para alguns cultivos específicos.
2. **Modelagem Preditiva**: Após o entendimento do conjunto, desenvolvemos e comparamos cinco modelos preditivos com algoritmos diferentes de Machine Learning. O objetivo de cada modelo é recomendar o melhor produto agrícola para plantio com base nas características atuais do solo e do clima. Avaliamos a performance de cada um através de métricas adequadas ao problema de classificação.

## 📁 Estrutura de pastas

- <b>aprendizado-de-maquina.ipynb</b>: Jupyter Notebook contendo toda a pipeline de dados, desde a análise exploratória (com os relatórios e os gráficos) até o treinamento e a avaliação dos 5 modelos preditivos criados.
- <b>produtos_agricolas.csv</b>: Base de dados com informações de solo e clima relacionadas aos produtos agrícolas.
- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Como executar o código

### Opção 1: Execução no Google Colab (Na nuvem)

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Faça o upload do arquivo `aprendizado-de-maquina.ipynb` presente nesta pasta.
3. Ao executar a terceira célula (referente à coleta de dados), o código solicitará interativamente o upload do dataset. Selecione o arquivo `produtos_agricolas.csv` que está presente nesta pasta.
4. Execute as células em sequência, observando as impressões de tela com análises em texto puro e a plotagem dos cinco gráficos exigidos, seguidos da seção de previsões em Machine Learning.

### Opção 2: Execução Local (Em sua máquina)

**Pré-requisitos:**

- Ter o Python 3 instalado.
- Ter o Jupyter Notebook ou JupyterLab instalado.
- Bibliotecas Python necessárias: `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn`.

**Passo a passo:**

1. Clone ou faça o download deste repositório para o seu computador.
2. Navegue até a pasta do projeto executando no terminal: `cd ANO1/FASE3/CAP10`.
3. Inicie o Jupyter com o comando:

   ```bash
   jupyter notebook aprendizado-de-maquina.ipynb
   ```

4. Execute as células em sequência. **Nota**: as instruções de upload contidas no código foram formuladas para o Colab (`google.colab import files`). Para executar 100% local, substitua a célula de upload localmente pelo carregamento direto do Pandas (`pd.read_csv('produtos_agricolas.csv')`) usando o dataset já incluso na pasta.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

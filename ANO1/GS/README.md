# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
</a>
</p>

<br>

# Modelo de Predição de Risco de Burnout em Funcionários

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

O projeto, desenvolvido no contexto da Global Solution - "O Futuro do Trabalho: Mais Humano, Inclusivo e Sustentável", apresenta um protótipo focado no eixo temático de **Monitoramento de bem-estar e saúde mental no trabalho**.

A solução proposta é um sistema capaz de realizar a predição e análise de risco de burnout em colaboradores, baseando-se em dados coletados sobre o ambiente de trabalho. Para fins desta prova de conceito, utiliza-se um *dataset* sintético com informações comportamentais e organizacionais que podem levar ao esgotamento profissional, incluindo: idade, horas de trabalho, interações noturnas, tempo sem férias, score de satisfação, entre outros indicadores.

## 📁 Estrutura de pastas

Dentre os arquivos presentes nesta pasta do projeto (GS), definem-se:

- <b>burnout_predictor.ipynb</b>: Notebook Jupyter contendo a coleta, análise exploratória de dados (EDA) e a modelagem preditiva com algoritmos de Machine Learning.

- <b>dataset_burnout_adjusted_5000.csv</b>: Base de dados com registros sintéticos simulando cenários e métricas organizacionais utilizadas para o treinamento e validação do modelo.

- <b>Global Solutions - Burnout Predictor.pdf</b>: Documentação e relatório completo detalhando o desenvolvimento, fundamentação teórica, as tomadas de decisões e as conclusões do projeto.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 📎 Links e Observações

- <b>Explicação de decisões técnicas</b>: Todo o detalhamento dos testes, análises dos dados, seleção de *features* e treinamento do modelo encontram-se documentados passo a passo no notebook `burnout_predictor.ipynb` e embasados teoricamente pelo documento em PDF anexo.
- <b>Observações Gerais</b>: O projeto possui finalidade acadêmica e visa promover inovações ligadas ao futuro do trabalho, saúde mental e estabelecimento de boas práticas de RH nas corporações.

## 🔧 Como executar o código

1. Faça o clone ou o download deste repositório para o seu ambiente local.
2. Certifique-se de ter um ambiente configurado para execução de notebooks Jupyter (como o Jupyter Lab, Anaconda, Visual Studio Code com extensão Jupyter ou Google Colab).
3. Caso opte por execução local, garanta que possui as bibliotecas da linguagem Python instaladas (geralmente `pandas`, `numpy`, `matplotlib`, `seaborn` e bibliotecas `scikit-learn`).
4. Abra o arquivo `burnout_predictor.ipynb` no ambiente de sua escolha.
5. Verifique se o caminho do arquivo `dataset_burnout_adjusted_5000.csv` apontado no momento da leitura (importação dos dados no pandas) corresponde corretamente ao mesmo diretório ou modifique a string de caminho, caso necessário.
6. Execute as células sequencialmente para reproduzir a análise e o treinamento do modelo de Machine Learning.

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

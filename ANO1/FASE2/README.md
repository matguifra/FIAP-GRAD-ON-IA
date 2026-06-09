# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="../../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

# 🚀 FASE 2 — IoT, Python e Análise Estatística no Agronegócio

## 📚 Graduação ON em Inteligência Artificial

## 👩🏻‍💻 Sobre esta Fase

Esta fase representa uma etapa da minha evolução na Graduação ON em Inteligência Artificial da FIAP.

Aqui estão organizados:

- 📖 Conteúdos teóricos estudados
- 🧠 Conceitos fundamentais consolidados
- 🛠 Tecnologias aplicadas
- 📂 Projetos desenvolvidos
- 📊 Resultados obtidos
- 🎯 Competências adquiridas

Esta documentação tem como objetivo demonstrar, de forma estruturada, o que foi aprendido e aplicado durante esta etapa do curso.

---

## 👥 Integrantes

| Nome | RM |
|---|---|
| Tales Ferraz de Arruda Domienikan | RM567483 |
| Leticia Angelim Guerra | RM567501 |
| Rivando Bezerra Cavalcanti Neto | RM568235 |
| Matheus Guimarães França | RM567144 |
| João Rafael Gonçalves Ramos | RM567908 |

---

## 🎯 Objetivo da Fase

Aplicar fundamentos de Sistemas Embarcados, Python e Análise Estatística em problemas reais do agronegócio, com foco em:

- Simular sistemas de IoT com sensores e atuadores em ambientes virtuais
- Integrar dispositivos a APIs externas e a serviços de armazenamento em nuvem
- Construir aplicações em Python para gestão e tomada de decisão
- Aplicar conceitos de banco de dados relacional e persistência em múltiplos formatos
- Realizar análise estatística e descritiva com a linguagem R

## 📖 Conteúdos Abordados

- Programação para sistemas embarcados em C++ (ESP32)
- Simulação de circuitos eletrônicos na plataforma Wokwi
- Comunicação com APIs REST (OpenWeatherMap) e cloud (ThingSpeak)
- Programação em Python: estruturas de dados, modularização e validação de entrada
- Persistência de dados em arquivos (TXT, JSON) e em banco de dados Oracle
- Operações CRUD com Oracle Database
- Linguagem R para análise estatística e visualização
- Estatística descritiva: medidas de tendência central, dispersão e separatrizes
- Tipos de variáveis (qualitativas e quantitativas) e fontes de dados públicas (IBGE, CONAB, MAPA)
- Introdução ao Machine Learning com Regressão Logística em R

## 🛠 Tecnologias Utilizadas

Durante esta fase, foram utilizadas as seguintes tecnologias:

- C++ e ESP32 (microcontrolador)
- Plataforma Wokwi (simulação)
- API OpenWeatherMap e ThingSpeak
- Python 3
- Oracle Database e biblioteca `oracledb`
- R e RStudio
- Bibliotecas R: `readxl`, `ggplot2`, `dplyr`

## 📂 Projetos Desenvolvidos

### 📌 Projeto 1 — FarmTech Solutions: Irrigação Inteligente com ESP32

**Descrição:**

Sistema de irrigação inteligente desenvolvido para a cultura de tomate, simulado em plataforma Wokwi com microcontrolador ESP32. O sistema monitora em tempo real os níveis de NPK (botões), pH do solo (sensor LDR), umidade do solo (DHT22) e exibe os dados em um display LCD. A bomba d'água só é acionada quando todas as condições ideais são atendidas. Para enriquecer os dados, o sistema busca informações climáticas em tempo real pela API OpenWeatherMap e envia as leituras para o ThingSpeak, formando um dataset histórico que alimenta um modelo de Regressão Logística treinado em R para evoluir a lógica de irrigação.

**Links do projeto:**

- 🎥 [Vídeo — Demonstração do Sistema](https://youtu.be/ZCE25_D37qg)

**Tecnologias utilizadas:**

- C++ e ESP32
- Plataforma Wokwi
- API OpenWeatherMap
- ThingSpeak (armazenamento em nuvem)
- R (análise de dados e modelo preditivo)
- Bibliotecas: `LiquidCrystal_I2C`, `DHT sensor library`, `ArduinoJson`

**Principais aprendizados:**

- Programação de microcontroladores e leitura de sensores analógicos e digitais
- Uso da técnica de PULLUP para tratamento de ruídos em botões
- Integração de dispositivos IoT com APIs REST externas
- Decodificação de dados JSON em ambiente embarcado
- Envio e armazenamento de séries temporais em nuvem
- Construção e validação de um modelo de Regressão Logística em R

---

### 📌 Projeto 2 — Sistema de Gestão de Colheita de Cana-de-Açúcar em Python

**Descrição:**

Aplicação em Python desenvolvida para gerenciar operações de colheita de cana-de-açúcar com foco em monitorar e alertar perdas no processo. O sistema permite cadastrar talhões, registrar operações, gerar relatórios e classificar automaticamente a taxa de perda em três níveis (alta acima de 15%, média entre 8% e 15%, baixa abaixo de 8%). Os dados podem ser persistidos em arquivos TXT, JSON ou diretamente em um banco de dados Oracle, com sincronização entre memória e banco.

**Tecnologias utilizadas:**

- Python 3
- Biblioteca `oracledb`
- Oracle Database
- Persistência em JSON e TXT

**Principais aprendizados:**

- Modularização de código Python em funções específicas
- Validação robusta de entrada de dados pelo usuário
- Manipulação de estruturas de dados (dicionários e listas) para representar entidades
- Persistência de dados em múltiplos formatos (TXT, JSON e Oracle)
- Operações DDL e DML em Oracle a partir de Python
- Geração de relatórios formatados com tabelas alinhadas

---

### 📌 Projeto 3 — Análise Estatística do Agronegócio com R

**Descrição:**

Projeto de Ciência de Dados aplicado ao agronegócio, com o objetivo de aplicar conceitos fundamentais de estatística descritiva sobre uma base de dados extraída de fontes públicas brasileiras (IBGE, CONAB e MAPA). A base, com pelo menos 30 instâncias, contempla variáveis qualitativas (nominal e ordinal) e quantitativas (discreta e contínua). Um script em R foi desenvolvido para carregar os dados, extrair medidas de tendência central, dispersão e separatrizes, e gerar visualizações de distribuições numéricas e categóricas.

**Tecnologias utilizadas:**

- R e RStudio
- Bibliotecas: `readxl`, `ggplot2`, `dplyr`
- Excel (base de dados estruturada)

**Principais aprendizados:**

- Coleta de dados em fontes públicas brasileiras do agronegócio
- Estruturação de bases de dados com diferentes tipos de variáveis
- Aplicação de estatística descritiva (média, mediana, desvio padrão, quartis)
- Geração de visualizações estéticas com `ggplot2`
- Documentação técnica de análises estatísticas

## 🧠 Competências Desenvolvidas

Ao final desta fase, consolidei:

- ✔️ Programação para sistemas embarcados (ESP32 e C++)
- ✔️ Integração de dispositivos IoT com APIs e serviços em nuvem
- ✔️ Desenvolvimento de aplicações em Python com persistência em múltiplos formatos
- ✔️ Modelagem e operação de bancos de dados Oracle a partir de Python
- ✔️ Programação em R para análise estatística e visualização
- ✔️ Aplicação prática de estatística descritiva em problemas reais
- ✔️ Construção e validação de modelos preditivos com Regressão Logística
- ✔️ Documentação técnica clara
- ✔️ Versionamento e organização de código

## 📋 Licença

Este projeto acadêmico segue o modelo de documentação FIAP.

MODELO GIT FIAP por FIAP está licenciado sob Attribution 4.0 International.

# Play na sua carreira em IA

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

## 📜 Descrição

A proposta deste trabalho, ambientado em uma startup fictícia chamada **FarmTech Solutions**, foi desenvolver uma aplicação em **Python** para auxiliar uma fazenda na migração para a Agricultura Digital.

A solução implementada suporta dois tipos de culturas, **soja** e **milho**, e é responsável por calcular:

- área de plantio;
- quantidade necessária de insumos;
- consumo estimado de água;
- dados de manejo agrícola.

A aplicação possui um menu interativo que permite:

- entrada de dados;
- consulta dos dados cadastrados;
- atualização de informações;
- remoção de registros;
- saída do programa.

Na sequência, foi criado um script em **R** para calcular dados estatísticos básicos com os dados gerados pela aplicação em Python, como média, mediana e desvio padrão.

## 📁 Estrutura de pastas

```text
cap1/
├── lavouras.py      # Script em Python para cálculos e gestão da lavoura
├── lavouras.R       # Script em R para análise estatística
└── README.md        # Documentação do CAP1
```

## 🔧 Como executar o código

### Pré-requisitos

- Python 3 instalado
- R instalado

### Passo a passo

1. Clone este repositório em sua máquina.

2. Acesse a pasta do projeto pelo terminal:

```bash
cd assets/fase1/cap1
```

3. Execute o script em Python:

```bash
python lavouras.py
```

4. Interaja com o menu no terminal para adicionar, consultar, atualizar ou remover dados das lavouras.

5. Execute o script em R para visualizar as estatísticas:

```bash
Rscript lavouras.R
```

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7**, permitindo visualizar diretamente:

- o código Python;
- o código R;
- a documentação do CAP1;
- os comandos de execução.

A integração ajuda a centralizar as entregas anteriores em uma única aplicação Streamlit.

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

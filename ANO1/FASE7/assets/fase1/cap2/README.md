# FIAP - Faculdade de Informática e Administração Paulista

# IA e seu mundo de possibilidades

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

O objetivo deste projeto foi desenvolver um modelo de **Inteligência Artificial** usando o **Teachable Machine**, do Google, para detectar e classificar automaticamente diferentes tipos de utensílios de cozinha a partir de imagens.

A atividade trabalhou conceitos iniciais de **visão computacional** e **aprendizado de máquina**, utilizando uma ferramenta acessível e visual para treinar um modelo de classificação de imagens.

O modelo foi treinado para reconhecer três classes:

- **Panelas**
- **Espátulas**
- **Assadeiras**

Os resultados, etapas de treinamento, testes e análise crítica estão documentados no arquivo `relatorio.pdf`.

---

## 🎯 Objetivo

Desenvolver um modelo capaz de classificar utensílios de cozinha a partir de imagens, avaliando sua precisão e observando o comportamento da IA diante de novos exemplos.

A proposta também teve como objetivo:

- compreender o funcionamento básico de modelos de classificação de imagens;
- utilizar o Teachable Machine para criar um projeto de IA;
- coletar e organizar imagens por categoria;
- testar o modelo com novas imagens;
- analisar acertos, limitações e possibilidades de melhoria.

---

## 🧠 Metodologia

O desenvolvimento foi dividido em quatro etapas principais:

1. **Coleta de imagens**  
   Foram reunidas imagens de panelas, espátulas e assadeiras.

2. **Organização das classes**  
   As imagens foram separadas em categorias dentro do Teachable Machine.

3. **Treinamento do modelo**  
   O modelo foi treinado usando as configurações avançadas da plataforma.

4. **Teste e avaliação**  
   Novas imagens foram usadas para verificar se o modelo conseguia classificar corretamente os utensílios.

---

## ⚙️ Configurações do Treinamento

| Parâmetro | Valor |
|---|---:|
| Epochs | 50 |
| Batch Size | 16 |
| Learning Rate | 0.001 |
| Classes | 3 |

---

## 📁 Estrutura de arquivos

```text
cap2/
├── project.tm       # Arquivo do projeto salvo no Teachable Machine
├── relatorio.pdf    # Relatório detalhado da atividade
└── README.md        # Documentação do CAP2
```

---

## 📦 Arquivos principais

### `project.tm`

Arquivo exportado do Teachable Machine contendo o projeto treinado, com as classes de imagens e as configurações utilizadas.

### `relatorio.pdf`

Documento com a explicação completa do projeto, incluindo:

- objetivos;
- metodologia;
- prints das etapas;
- configuração do treinamento;
- taxa de acurácia;
- matriz de confusão;
- testes realizados;
- análise crítica;
- sugestões de melhorias.

---

## 🔧 Como executar

### Pré-requisitos

- Navegador web compatível;
- Acesso ao [Teachable Machine](https://teachablemachine.withgoogle.com/);
- Leitor de PDF para visualizar o relatório.

### Passo a passo

1. Abra o arquivo `relatorio.pdf` para entender o desenvolvimento do projeto.

2. Acesse o Teachable Machine:

```text
https://teachablemachine.withgoogle.com/
```

3. Selecione a opção:

```text
Classificação de Imagem
```

4. Escolha a opção para abrir um projeto existente.

5. Faça o upload do arquivo:

```text
project.tm
```

6. Teste novas imagens usando a webcam ou fazendo upload direto na plataforma.

---

## 📊 Resultados

O modelo apresentou bom desempenho na classificação das três classes avaliadas.

As categorias de panelas, espátulas e assadeiras possuem características visuais relativamente distintas, o que contribuiu para uma boa separação entre as classes.

Mesmo assim, o modelo pode apresentar limitações em situações como:

- imagens com baixa iluminação;
- objetos em ângulos difíceis;
- fundos poluídos;
- utensílios visualmente parecidos;
- exemplos muito diferentes dos usados no treinamento.

---

## 🚀 Possíveis melhorias

Para melhorar o modelo, poderiam ser realizadas as seguintes ações:

- aumentar a quantidade de imagens por classe;
- usar imagens reais em ambientes variados;
- testar diferentes fundos e iluminações;
- incluir mais categorias de utensílios;
- adicionar uma classe para “outros objetos”;
- testar novos valores de epochs, batch size e learning rate.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo do CAP2;
- relatório PDF;
- arquivo do modelo `project.tm`;
- README do capítulo.

Essa integração ajuda a consolidar as entregas das fases anteriores em uma única aplicação Streamlit.

---

## ✅ Status

| Item | Status |
|---|---|
| Coleta de imagens | ✅ Concluída |
| Treinamento no Teachable Machine | ✅ Concluído |
| Testes e avaliação | ✅ Concluídos |
| Relatório PDF | ✅ Concluído |
| Arquivo `project.tm` | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

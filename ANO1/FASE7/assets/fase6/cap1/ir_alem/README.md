# Fase 6 - Ir Além: Transfer Learning e Fine Tuning

## FarmTech Solutions

## 👨‍🎓 Integrantes

| Nome | RM |
|---|---|
| Leticia Angelim Guerra | RM567501 |
| Rivando Bezerra Cavalcanti Neto | RM568235 |
| Tales Ferraz de Arruda Domienikan | RM567483 |
| Matheus Guimarães França | RM567144 |
| João Rafael Gonçalves Ramos | RM567908 |

---

## 📜 Descrição

Este projeto corresponde à opção **3.2 - Transfer Learning e Fine Tuning** do projeto **Ir Além** da Fase 6.

A proposta foi comparar abordagens de classificação de imagens usando o dataset binário `cow` vs `dog`, avaliando se uma rede pré-treinada apresenta melhor desempenho do que uma rede treinada do zero e se a remoção do fundo das imagens melhora a classificação.

O projeto utiliza **MobileNetV2**, pré-treinada na ImageNet, com fine tuning das últimas camadas para adaptar o modelo ao domínio específico do problema.

---

## 🎯 Objetivo

O objetivo principal foi avaliar o impacto de **Transfer Learning**, **Fine Tuning** e **segmentação de fundo** em um dataset pequeno de classificação binária.

As hipóteses avaliadas foram:

1. Redes pré-treinadas superam redes treinadas do zero?
2. A remoção do fundo das imagens melhora a classificação?
3. O contexto visual do ambiente ajuda ou atrapalha o modelo?

---

## 🐄🐕 Dataset

O dataset utilizado contém imagens de duas classes:

| Classe | Descrição |
|---|---|
| `cow` | Vaca |
| `dog` | Cachorro |

A estrutura esperada do dataset no Google Drive é:

```text
MyDrive/dataset-classificacao/
├── train/
│   ├── cow/
│   └── dog/
├── val/
│   ├── cow/
│   └── dog/
└── test/
    ├── cow/
    └── dog/
```

A divisão usada foi:

| Split | Cow | Dog |
|---|---:|---:|
| Treino | 32 | 32 |
| Validação | 4 | 4 |
| Teste | 4 | 4 |

---

## 🧠 Estratégia Técnica

### Modelo Base

O modelo utilizado foi:

```text
MobileNetV2
```

A MobileNetV2 foi escolhida por equilibrar bom desempenho e eficiência computacional. Como ela já foi treinada na ImageNet, possui filtros capazes de reconhecer bordas, texturas, formas e padrões visuais úteis para classificação de imagens.

Essa escolha é especialmente importante porque o dataset usado no projeto é pequeno.

---

## 🔁 Transfer Learning

Na primeira etapa, a MobileNetV2 foi usada como extratora de características.

A estratégia foi:

- carregar a MobileNetV2 pré-treinada na ImageNet;
- congelar as camadas da rede base;
- adicionar uma camada final de classificação binária;
- treinar apenas a nova camada final;
- avaliar o desempenho em treino, validação e teste.

Essa abordagem permite reaproveitar o conhecimento aprendido em milhões de imagens sem precisar treinar uma rede do zero.

---

## 🔧 Fine Tuning

Na segunda etapa, foi aplicado **Fine Tuning**.

A estratégia foi:

- descongelar as últimas 20 camadas da MobileNetV2;
- usar taxa de aprendizado reduzida;
- treinar por mais algumas épocas;
- adaptar as camadas finais ao problema específico `cow` vs `dog`.

Essa técnica preserva o conhecimento visual geral da rede e ajusta apenas representações mais específicas.

---

## 🖼️ Segmentação com rembg

Também foi criado um dataset paralelo com fundo removido usando a biblioteca:

```text
rembg
```

A `rembg` utiliza o modelo U²-Net para separar o primeiro plano do fundo da imagem.

O objetivo foi verificar se remover o background ajudaria o modelo a focar apenas no animal.

O experimento comparou:

- imagens originais;
- imagens com fundo removido.

---

## 🏗️ Arquitetura do Projeto

O fluxo geral do projeto é:

```text
Dataset original cow/dog
        ↓
Separação em treino, validação e teste
        ↓
Caminho 1: imagens originais
Caminho 2: imagens com fundo removido
        ↓
MobileNetV2 pré-treinada na ImageNet
        ↓
Transfer Learning
        ↓
Fine Tuning nas últimas camadas
        ↓
Avaliação dos resultados
```

A imagem da arquitetura está em:

```text
assets/arquitetura.svg
```

---

## 📊 Resultados

| Abordagem | Treino | Validação | Teste | Tempo |
|---|---:|---:|---:|---:|
| Transfer Learning - imagens originais | 100% | 87,5% | 100% | ~41s |
| Transfer Learning + Fine Tuning | 100% | 100% | 100% | ~30s |
| Transfer Learning - imagens sem fundo | 100% | 100% | 87,5% | ~40s |

---

## 📌 Análise dos Resultados

O melhor resultado foi obtido com **Transfer Learning + Fine Tuning**, alcançando 100% de acurácia no conjunto de teste.

A remoção do fundo não melhorou o desempenho. Pelo contrário, o teste com imagens sem fundo caiu para 87,5%.

Isso indica que o contexto visual das imagens pode ter ajudado a MobileNetV2 na classificação, já que a rede foi originalmente treinada em imagens naturais da ImageNet, onde animais costumam aparecer em ambientes reais.

Também é importante observar que o conjunto de teste contém apenas 8 imagens, então as métricas podem variar bastante com poucas classificações erradas.

---

## ⚠️ Limitações

As principais limitações do experimento foram:

- dataset pequeno;
- apenas 8 imagens no conjunto de teste;
- classes visualmente muito distintas;
- avaliação baseada principalmente em acurácia;
- ausência de data augmentation;
- segmentação automática sem entendimento semântico completo.

Em projetos maiores, seria recomendado usar mais imagens, aplicar data augmentation e avaliar métricas como precision, recall e F1-score.

---

## 🎥 Vídeo Demonstrativo

O vídeo demonstrativo está disponível em:

```text
https://youtu.be/0Ky0SZkz3NI
```

---

## 📓 Notebook

O notebook principal do projeto é:

```text
LeticiaAngelimGuerra_rm567501_pbl_fase6_ir_alem.ipynb
```

Ele contém:

- carregamento do dataset;
- preparação das imagens;
- aplicação de Transfer Learning;
- Fine Tuning;
- remoção de fundo com `rembg`;
- treinamento dos modelos;
- comparação dos resultados.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal;
- **TensorFlow / Keras** — treinamento do modelo;
- **MobileNetV2** — modelo pré-treinado;
- **ImageNet** — base original de pré-treinamento;
- **rembg** — remoção automática de fundo;
- **U²-Net** — modelo usado pela rembg;
- **Google Colab** — ambiente de execução;
- **Google Drive** — armazenamento do dataset;
- **Jupyter Notebook** — desenvolvimento da solução.

---

## 📁 Estrutura de Arquivos

```text
ir_alem/
├── README.md
├── LeticiaAngelimGuerra_rm567501_pbl_fase6_ir_alem.ipynb
└── assets/
    └── arquitetura.svg
```

---

## ▶️ Como Executar

### 1. Preparar o dataset no Google Drive

Organize as imagens nesta estrutura:

```text
MyDrive/dataset-classificacao/
├── train/
│   ├── cow/
│   └── dog/
├── val/
│   ├── cow/
│   └── dog/
└── test/
    ├── cow/
    └── dog/
```

### 2. Abrir o notebook no Google Colab

Abra o arquivo:

```text
LeticiaAngelimGuerra_rm567501_pbl_fase6_ir_alem.ipynb
```

### 3. Montar o Google Drive

Execute as células iniciais para montar o Drive e acessar o dataset.

### 4. Instalar dependências

O notebook instala as bibliotecas necessárias.

> Atenção: após instalar `rembg`, pode ser necessário reiniciar o runtime do Colab e executar novamente a partir da célula de imports.

### 5. Executar o pipeline

Execute as células em sequência para:

- carregar os dados;
- treinar com imagens originais;
- aplicar Fine Tuning;
- gerar imagens sem fundo;
- treinar com o dataset segmentado;
- comparar os resultados.

---

## 📌 Integração com a Fase 7

Este projeto Ir Além foi integrado à dashboard central da **Fase 7** do FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo da proposta;
- arquitetura do projeto;
- notebook do Ir Além;
- README da entrega;
- resultados comparativos;
- vídeo demonstrativo.

Essa integração permite consultar o projeto complementar da Fase 6 dentro da aplicação final centralizada.

---

## ✅ Status

| Item | Status |
|---|---|
| Dataset cow/dog | ✅ Organizado |
| Transfer Learning | ✅ Concluído |
| Fine Tuning | ✅ Concluído |
| Segmentação com rembg | ✅ Concluída |
| Comparação dos resultados | ✅ Concluída |
| Notebook | ✅ Disponível |
| Arquitetura | ✅ Disponível |
| Vídeo demonstrativo | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

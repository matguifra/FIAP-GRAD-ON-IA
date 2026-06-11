# FIAP - Faculdade de Informática e Administração Paulista

# Cap 6 - Python e Além

## Grupo 15

## 👨‍🎓 Integrantes

- João Rafael Gonçalves Ramos
- Letícia Angelim Guerra
- Matheus Guimarães França
- Rivando Bezerra Cavalcanti Neto
- Tales Ferraz de Arruda Domienikan

## 👩‍🏫 Professores

### Tutor(a)

- Ana Cristina dos Santos

### Coordenador(a)

- André Godoi Chiovato

---

## 📜 Descrição

Este projeto foi desenvolvido no contexto da **FarmTech Solutions**, com foco na criação de um sistema em **Python** para apoiar a gestão de operações de colheita no agronegócio.

A solução trabalha com o cenário da **colheita de cana-de-açúcar**, permitindo cadastrar talhões, registrar operações de colheita, calcular alertas de perda e salvar os dados em diferentes formatos.

O sistema foi pensado para apoiar o agricultor na tomada de decisão, indicando quando a taxa de perda da colheita está dentro de um nível aceitável ou quando exige atenção.

---

## 🎯 Objetivo

O objetivo principal deste CAP foi desenvolver uma aplicação em Python capaz de:

- cadastrar talhões agrícolas;
- listar talhões cadastrados;
- registrar operações de colheita;
- calcular alertas de perda;
- gerar relatório em arquivo `.txt`;
- salvar e carregar dados em `.json`;
- integrar os dados com banco de dados Oracle;
- validar entradas do usuário;
- organizar os dados em estruturas como dicionários e listas.

---

## 🌱 Contexto Agrícola

O agronegócio envolve uma cadeia produtiva ampla, incluindo produção, processamento, distribuição, logística, tecnologia e serviços de apoio.

No caso da cana-de-açúcar, mesmo com mecanização e uso de tecnologia no campo, ainda podem ocorrer perdas durante a colheita. Essas perdas impactam diretamente a produtividade, o custo operacional e o resultado financeiro do produtor.

Por isso, o sistema desenvolvido busca registrar operações de colheita e classificar a perda em três níveis:

| Faixa de perda | Classificação |
|---|---|
| Menor que 8% | Baixa |
| Entre 8% e 15% | Média |
| Maior que 15% | Alta |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — desenvolvimento da aplicação principal;
- **Oracle Database** — persistência dos dados;
- **oracledb** — biblioteca Python para conexão com Oracle;
- **JSON** — armazenamento local dos dados;
- **TXT** — geração de relatório;
- **Terminal / Console** — interação com o usuário.

---

## 📁 Estrutura de Arquivos

```text
cap6/
├── app.py                              # Sistema principal em Python
├── referencia de configuracao Oracle   # Referência de configuração para Oracle
└── README.md                           # Documentação do CAP6
```

---

## 🔧 Como Executar o Código

### Pré-requisitos

- Python 3 instalado;
- Biblioteca `oracledb` instalada;
- Oracle configurado, caso deseje usar a integração com banco de dados.

Para instalar a dependência principal:

```bash
pip install oracledb
```

### Execução

Acesse a pasta do CAP6:

```bash
cd assets/fase2/cap6
```

Execute o sistema:

```bash
python app.py
```

---

## 🧭 Funcionamento Geral

Ao executar o arquivo `app.py`, a função principal inicia um menu interativo no terminal.

Cada opção do menu aciona uma funcionalidade específica do sistema, permitindo ao usuário cadastrar, consultar, registrar, exportar e sincronizar dados.

O sistema mantém os dados em memória por meio de um dicionário principal com duas chaves:

```text
db = {
  "talhoes": {},
  "operacoes": []
}
```

- `talhoes`: armazena os talhões cadastrados;
- `operacoes`: armazena as operações de colheita realizadas.

---

## 📌 Funcionalidades do Menu

### 1. Cadastrar Talhão

Permite cadastrar um novo talhão agrícola informando:

- ID;
- nome;
- área.

O sistema valida os dados inseridos e armazena as informações no banco em memória.

---

### 2. Listar Talhões

Exibe todos os talhões cadastrados em formato de tabela no terminal.

Caso não existam talhões cadastrados, o sistema informa o usuário e cancela a operação.

---

### 3. Registrar Operação

Registra uma operação de colheita vinculada a um talhão.

O usuário informa:

- talhão;
- data da operação;
- peso colhido;
- percentual de perda.

Com base no percentual de perda, o sistema gera automaticamente um alerta:

- **Baixa**
- **Média**
- **Alta**

---

### 4. Listar Operações

Exibe as operações de colheita já registradas, incluindo:

- ID;
- data;
- talhão;
- peso colhido;
- percentual de perda;
- nível de alerta.

---

### 5. Gerar Relatório

Gera um arquivo `relatorio.txt` com resumo das operações registradas.

O relatório inclui métricas como:

- total de operações;
- soma do peso colhido;
- média de perda;
- tabela com os dados das operações.

---

### 6. Salvar JSON

Salva os dados atuais do sistema em um arquivo `.json`, permitindo persistência local das informações.

---

### 7. Carregar JSON

Carrega dados previamente salvos em um arquivo `.json`, restaurando os talhões e operações para uso no sistema.

---

### 8. Sincronizar com Oracle

Permite sincronizar os dados armazenados em memória com um banco de dados Oracle.

O sistema verifica se as credenciais estão configuradas por variáveis de ambiente:

```text
ORA_USER
ORA_PASS
ORA_DSN
```

Caso as credenciais não estejam definidas, o programa solicita os dados ao usuário.

---

## 🗄️ Integração com Oracle

A integração com Oracle permite criar tabelas e sincronizar registros de talhões e operações.

O sistema possui funções para:

- verificar se a configuração Oracle está disponível;
- solicitar credenciais ao usuário;
- criar tabelas no banco;
- listar talhões salvos no Oracle;
- listar operações salvas no Oracle;
- inserir novos registros sem duplicar dados.

Essa integração aproxima a aplicação de um cenário real de persistência de dados em ambiente corporativo.

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento deste CAP, foram aplicados os seguintes conceitos:

- funções em Python;
- dicionários;
- listas;
- validação de entrada;
- manipulação de arquivos TXT;
- manipulação de arquivos JSON;
- conexão com banco de dados;
- variáveis de ambiente;
- CRUD;
- organização de dados agrícolas;
- lógica de alertas.

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7** do projeto FarmTech Solutions.

Na dashboard, é possível visualizar:

- resumo do CAP6;
- código principal em Python;
- referência de configuração Oracle;
- comandos de execução;
- explicação do sistema.

Essa integração ajuda a consolidar os materiais da Fase 2 dentro de uma aplicação única em Streamlit.

---

## ✅ Status

| Item | Status |
|---|---|
| Sistema Python | ✅ Concluído |
| Cadastro de talhões | ✅ Concluído |
| Registro de operações | ✅ Concluído |
| Relatório TXT | ✅ Concluído |
| Persistência JSON | ✅ Concluída |
| Integração Oracle | ✅ Implementada |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

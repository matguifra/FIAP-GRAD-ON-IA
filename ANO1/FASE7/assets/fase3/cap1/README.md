# Fase 3 - CAP1: Banco de Dados Oracle

## FarmTech Solutions

## 👨‍🎓 Integrantes

- João Rafael Gonçalves Ramos
- Letícia Angelim Guerra
- Matheus Guimarães França
- Rivando Bezerra Cavalcanti Neto
- Tales Ferraz de Arruda Domienikan

---

## 📜 Descrição

Nesta etapa do projeto **FarmTech Solutions**, o foco foi estruturar um banco de dados **Oracle** para armazenar, consultar e analisar informações coletadas por sensores agrícolas.

Os dados utilizados foram gerados a partir de medições simuladas de sensores, incluindo informações sobre pH do solo, umidade do solo, temperatura, nutrientes NPK, umidade do ar e status da bomba de irrigação.

Além da parte de banco de dados, este CAP também inclui entregas do **Programa Ir Além**, com dashboard em Python e aplicação de Machine Learning no contexto agrícola.

---

## 🎯 Objetivos

Os principais objetivos deste CAP foram:

- estruturar uma tabela relacional no Oracle;
- importar uma base CSV com leituras de sensores;
- executar consultas SQL para validação e análise dos dados;
- aplicar filtros, ordenações e funções estatísticas;
- registrar evidências do processo no Oracle SQL Developer;
- desenvolver entregas complementares do Programa Ir Além.

---

## 📊 Conjunto de Dados

O arquivo utilizado foi:

```text
data/dados_sensores.csv
```

A base contém **48 leituras simuladas**, registradas em intervalos de **5 minutos**, cobrindo aproximadamente **4 horas** de monitoramento.

### Variáveis principais

- `created_at` — data e horário da leitura;
- `ph_solo` — pH do solo;
- `umidade_solo` — umidade do solo;
- `nitrogenio` — nível de nitrogênio;
- `fosforo` — nível de fósforo;
- `potassio` — nível de potássio;
- `status_bomba` — indicador de bomba ligada ou desligada;
- `temperatura` — temperatura ambiente;
- `sensacao_termica` — sensação térmica;
- `umidade_ar` — umidade do ar.

---

## 🗄️ Estrutura da Tabela Oracle

A tabela criada no Oracle recebeu o nome:

```text
SENSORES_FARMTECH
```

### DDL da tabela

```sql
CREATE TABLE SENSORES_FARMTECH (
  CREATED_AT        TIMESTAMP,
  PH_SOLO           NUMBER(4,2),
  UMIDADE_SOLO      NUMBER(5,1),
  NITROGENIO        NUMBER(5,0),
  FOSFORO           NUMBER(5,0),
  POTASSIO          NUMBER(5,0),
  STATUS_BOMBA      NUMBER(1,0),
  TEMPERATURA       NUMBER(4,1),
  SENSACAO_TERMICA  NUMBER(4,1),
  UMIDADE_AR        NUMBER(4,1)
);
```

A escolha dos tipos considera a natureza das leituras:

- `TIMESTAMP` para preservar data e horário;
- `NUMBER` com casas decimais para medições como pH e umidade;
- inteiros para indicadores e valores discretos, como `STATUS_BOMBA`.

---

## 🔎 Consultas SQL Executadas

As consultas foram utilizadas para validar a importação dos dados e extrair informações úteis da base.

### Verificação da importação

```sql
SELECT * FROM SENSORES_FARMTECH
FETCH FIRST 20 ROWS ONLY;
```

### Filtro por umidade do solo

```sql
SELECT *
FROM SENSORES_FARMTECH
WHERE UMIDADE_SOLO > 70
ORDER BY CREATED_AT;
```

### Ordenação por pH

```sql
SELECT *
FROM SENSORES_FARMTECH
ORDER BY PH_SOLO DESC
FETCH FIRST 10 ROWS ONLY;
```

### Estatísticas da umidade

```sql
SELECT
  ROUND(AVG(UMIDADE_SOLO), 2) AS MEDIA_UMIDADE,
  MAX(UMIDADE_SOLO) AS MAX_UMIDADE,
  MIN(UMIDADE_SOLO) AS MIN_UMIDADE
FROM SENSORES_FARMTECH;
```

---

## 📈 Resultados Obtidos

A consulta estatística sobre a variável **UMIDADE_SOLO** retornou:

| Métrica | Valor |
|---|---:|
| Média da umidade do solo | 58,93% |
| Máxima registrada | 79,2% |
| Mínima registrada | 37,8% |

Esses resultados mostram a variação da umidade do solo durante o período analisado.

Valores abaixo de 60% indicam momentos em que a irrigação poderia ser acionada, enquanto valores acima de 70% indicam solo mais úmido e bomba possivelmente desligada.

---

## 🧾 Evidências

As evidências do processo foram salvas na pasta:

```text
docs/
```

Essa pasta contém prints do Oracle SQL Developer, incluindo:

- importação do CSV;
- escolha das colunas;
- definição dos tipos;
- confirmação da importação;
- execução das consultas SQL;
- resultados das análises.

---

## 🚀 Programa Ir Além 1 - Dashboard em Python

Além da atividade principal com Oracle, também foi desenvolvido um dashboard em Python para visualização dos dados de sensores agrícolas.

O dashboard apresenta:

- métricas principais dos sensores;
- gráficos interativos;
- análise temporal;
- recomendações de irrigação com base nas leituras.

### Vídeo demonstrativo

```text
https://youtu.be/J9iB4t9So8U
```

---

## 🧠 Programa Ir Além 2 - Machine Learning no Agro

O Ir Além 2 apresenta uma entrega complementar com aplicação de **Machine Learning** no contexto agrícola.

A entrega foi disponibilizada em formato de notebook, com foco em análise e aplicação de modelos no agronegócio.

### Vídeo demonstrativo

```text
https://youtu.be/pic7SCPDPn0
```

---

## 🎥 Vídeo Demonstrativo do CAP1

O vídeo principal da atividade pode ser acessado em:

```text
https://youtu.be/Txpuv0JD0wU
```

---

## 📁 Estrutura de Arquivos

```text
cap1/
├── data/
│   └── dados_sensores.csv
├── docs/
│   ├── print_import_columns.png
│   ├── print_import_definition.png
│   ├── print_import_sucess.png
│   ├── print_select.png
│   ├── print_where.png
│   ├── print_orderby.png
│   ├── print_stats.png
│   ├── print1.png
│   ├── print2.png
│   └── print3.png
├── src/
│   └── consultas.sql
├── ir-alem-2.ipynb
└── README.md
```

---

## 🔧 Como Executar / Consultar

### Consultar o CSV

O arquivo de dados está em:

```text
assets/fase3/cap1/data/dados_sensores.csv
```

### Consultar as queries SQL

O arquivo de consultas está em:

```text
assets/fase3/cap1/src/consultas.sql
```

### Visualizar evidências

Os prints estão em:

```text
assets/fase3/cap1/docs/
```

### Rodar pela dashboard da Fase 7

Na raiz do projeto, execute:

```bash
streamlit run app.py
```

Depois acesse:

```text
Fase 3 - Banco de Dados Estruturado > CAP1
```

---

## 📌 Integração com a Fase 7

Este CAP foi integrado à dashboard central da **Fase 7**, permitindo visualizar:

- dados dos sensores;
- consultas SQL;
- prints e evidências;
- vídeos demonstrativos;
- materiais do Programa Ir Além;
- README do CAP1.

Essa integração permite que os materiais da Fase 3 sejam consultados dentro de uma aplicação única em Streamlit.

---

## ✅ Status

| Item | Status |
|---|---|
| Base CSV | ✅ Concluída |
| Tabela Oracle | ✅ Criada |
| Consultas SQL | ✅ Concluídas |
| Evidências em prints | ✅ Concluídas |
| Ir Além 1 | ✅ Concluído |
| Ir Além 2 | ✅ Concluído |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.

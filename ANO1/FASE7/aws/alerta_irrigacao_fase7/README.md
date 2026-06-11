## Descrição

Este módulo implementa um **serviço de mensageria inteligente** integrado à infraestrutura AWS, responsável por monitorar os dados dos sensores agrícolas e disparar alertas automáticos para os funcionários da fazenda sempre que condições críticas forem detectadas.

O sistema lê os dados do arquivo `dados_sensores.csv` (gerado na Fase 1) e analisa os seguintes parâmetros:

| Parâmetro | Condição Crítica / Regra de Alerta |
|---|---|
| **pH** | Abaixo de 4.5 ou acima de 7.5 |
| **NPK** | N < 8, P < 80 ou K < 80 com a bomba ligada |
| **Umidade** | Abaixo de 20% |

---

## Infraestrutura AWS (Fase 5 → Fase 7)

O serviço utiliza o **AWS SNS (Simple Notification Service)** hospedado na região **América do Sul (São Paulo) — `sa-east-1`**, em conformidade com a decisão arquitetural e de segurança definida na Fase 5 do projeto.

### Configuração utilizada no provedor cloud:

| Campo | Valor Configurado |
|---|---|
| **Serviço** | AWS SNS |
| **Região** | sa-east-1 (São Paulo) |
| **Nome do Tópico** | AlertasAgroFiap |
| **Protocolo de Entrega** | E-mail |

---

## Modos de Execução (Tratamento de Falhas e Resiliência)

O sistema foi desenvolvido com dois modos de execução automáticos, prevendo diferentes ambientes de infraestrutura (como a máquina local dos desenvolvedores x máquina do avaliador).

### ✅ Modo Real (Infraestrutura Configurada)
- Conecta nativamente ao AWS SNS via `boto3`
- Dispara e-mail real para os encarregados da fazenda
- Exibe o `MessageId` retornado pela AWS como confirmação, garantindo rastreabilidade

### 🔁 Modo Simulação (Fallback Automático)
- Ativado automaticamente caso não existam credenciais IAM configuradas ou haja bloqueio de rede
- Exibe no terminal a mensagem que seria enviada
- Garante que o código não quebre em ambientes sem configuração

>  **Decisão Arquitetural:** Essa abordagem de fallback automático garante **resiliência e portabilidade**, permitindo que o sistema funcione tanto na nuvem quanto em ambientes não configurados.

---

##  Modelos de Mensagens (Alertas)

### 🛑 Alerta de pH Crítico (Anomalia Severa)

Disparado quando o pH do solo sai da faixa segura (4.5 – 7.5), indicando ação corretiva necessária.

```text
🛑 ALERTA DE PH CRÍTICO

Tempo: 117299.0 ms
O Nível de pH atingiu 2.5 (Fora do limite seguro de 4.5 - 7.5).

AÇÃO: Enviar equipe ao setor para correção de solo (calcário/enxofre).

---

# ⚠️ Alerta de Irrigação Deficiente (Falha de Manejo)

Disparado quando a bomba é ligada com níveis de NPK abaixo do ideal.

> **⚠️ ALERTA: IRRIGAÇÃO DEFICIENTE**
> 
> A bomba de irrigação foi **LIGADA**, porém os nutrientes (NPK) estão **BAIXOS**.
> 
> **AÇÃO:** Adicionar NPK imediatamente para não lavar o solo.

---

## Como Executar o Sistema

### 1. Pré-requisitos
Instale as dependências necessárias executando o comando abaixo:
```bash
pip install boto3 pandas awscli
```

### 2. Com AWS configurada (Envio real)
Configure suas credenciais da AWS:
```bash
aws configure
# Preencher:
# AWS Access Key ID: [Sua Access Key]
# AWS Secret Access Key: [Sua Secret Key]
# Default region name: sa-east-1
# Default output format: json
```

Em seguida, execute o script:
```bash
cd alerta_irrigacao_fase7
python alerta_irrigacao_aws.py
```

### 3. Sem AWS (Modo simulação)
Caso não queira configurar a AWS agora, basta rodar o script diretamente:
```bash
cd alerta_irrigacao_fase7
python alerta_irrigacao_aws.py
```
> *O sistema detecta automaticamente a ausência de credenciais e entra em modo simulação.*

---

##  Evidências de Funcionamento (AWS)


1️⃣ **Tópico SNS criado**  
*( print mostrando o ARN do tópico)*

2️⃣ **Assinatura confirmada**  
*( print com status "Confirmado")*

3️⃣ **Execução com envio real**  
*( print do terminal com sucesso + MessageId)*

4️⃣ **E-mail recebido**  
*( print da caixa de entrada com o alerta)*

---

## Tecnologias Utilizadas

| Tecnologia | Aplicação |
| :--- | :--- |
| **Python 3** | Lógica do sistema |
| **Pandas** | Leitura e análise do CSV |
| **Boto3** | Integração com AWS |
| **AWS SNS** | Envio de alertas |
| **AWS IAM / CLI** | Gerenciamento de credenciais |


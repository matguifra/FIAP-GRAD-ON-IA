import pandas as pd
import boto3
import os

# 1. LEITURA DOS DADOS (CSV da Fase 1)

def ler_dados_sensor(caminho_csv='dados_sensores.csv'):
    try:
        df = pd.read_csv(caminho_csv)
        ultima_leitura = df.iloc[-1] # Pega a última linha do arquivo
        
        return {
            "tempo_ms": ultima_leitura['tempo_ms'],
            "ph":       ultima_leitura['ph'],
            "umidade":  ultima_leitura['umidade'],
            "N":        ultima_leitura['N'],
            "P":        ultima_leitura['P'],
            "K":        ultima_leitura['K'],
            "bomba":    ultima_leitura['bomba']
        }
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return None

# 2. LÓGICA DE ALERTA 

def verificar_alertas(dados):
    # Avaliando os cenários dos dados
    umidade_baixa = dados['umidade'] < 20    # Considera baixo menor que 20%
    npk_ok = dados['N'] > 8 and dados['P'] > 80 and dados['K'] > 80 # Valores baseados na média da tabela
    
    # REGRA 1: Bomba ligada, mas o NPK (adubação) está crítico!
    if dados['bomba'] == 1 and not npk_ok:
        mensagem = (
            "⚠️ ALERTA: IRRIGAÇÃO DEFICIENTE\n\n"
            f"Tempo: {dados['tempo_ms']} ms\n"
            f"A bomba de irrigação foi LIGADA (Umidade={dados['umidade']}%), "
            f"porém os nutrientes estão BAIXOS no tanque.\n\n"
            f"Leitura NPK Atual:\n"
            f"N: {dados['N']} | P: {dados['P']} | K: {dados['K']}\n\n"
            "AÇÃO: Adicionar NPK imediatamente para não lavar o solo."
        )
        return "ALERTA_MENSAGERIA", mensagem
    
    # REGRA 2: PH extremamente ácido ou alcalino
    elif dados['ph'] < 4.5 or dados['ph'] > 7.5:
        mensagem = (
            "🛑 ALERTA DE PH CRÍTICO\n\n"
            f"Tempo: {dados['tempo_ms']} ms\n"
            f"O Nível de pH atingiu {dados['ph']} (Fora do limite seguro de 4.5 - 7.5).\n\n"
            "AÇÃO: Enviar equipe ao setor para correção de solo (calcário/enxofre)."
        )
        return "ALERTA_MENSAGERIA", mensagem

    # Tudo OK!
    else:
        return "TUDO_OK", None


# 3. CONEXÃO COM A AWS (Simulação + Real)

def enviar_alerta(mensagem):
    aws_key = os.getenv('AWS_ACCESS_KEY_ID')

    if aws_key:
        print("-> Conectando na AWS SNS...")
        sns = boto3.client('sns', region_name='sa-east-1')
        topico_arn = 'arn:aws:sns:sa-east-1:108703089725:AlertasAgroFiap'
        
        sns.publish(
            TopicArn=topico_arn,
            Message=mensagem,
            Subject='ALERTA SISTEMA AGRO'
        )
        print("✅ E-mail/SMS enviado pela AWS com sucesso!")
    else:
     
        print("\n" + "="*50)
        print("☁️  GERENCIADOR DE ALERTAS AWS SNS (Modo Simulação local)")
        print("Mensagem que chegaria no celular do fazendeiro:")
        print("-" * 50)
        print(mensagem)
        print("="*50 + "\n")


# 4. EXECUTANDO O PROGRAMA

if __name__ == "__main__":
    print("🌱 Iniciando Módulo de Mensageria (Fase 7)...")
    dados_atuais = ler_dados_sensor('dados_sensores.csv')
    
    if dados_atuais:
        status, mensagem = verificar_alertas(dados_atuais)
        
        if status == "ALERTA_MENSAGERIA":
            enviar_alerta(mensagem)
        else:
            print("✅ Condições de plantio ideais. Nenhum alerta necessário no momento.")

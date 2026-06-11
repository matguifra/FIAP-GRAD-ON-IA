from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"

FASE5_DIR = ASSETS_DIR / "fase5"
CAP1_DIR = FASE5_DIR / "cap1"

README_FILE = CAP1_DIR / "README.md"
CROP_YIELD = CAP1_DIR / "crop_yield.csv"
NOTEBOOK_EXECUTED = CAP1_DIR / "executed_notebook.ipynb"
NOTEBOOK_PBL = CAP1_DIR / "RivandoBezerra_rm568235_pbl_fase4.ipynb"
IR_ALEM = CAP1_DIR / "ir_alem"
ROTEIRO_VIDEO = CAP1_DIR / "ROTEIRO_VIDEO.md"
IMAGENS_DIR = CAP1_DIR / "ATV5_2"

AWS_DIR = BASE_DIR / "aws" / "alerta_irrigacao_fase7"

ALERTA_SCRIPT = AWS_DIR / "alerta_irrigacao_aws.py"
ALERTA_CSV = AWS_DIR / "dados_sensores.csv"
ALERTA_README = AWS_DIR / "README.md"
ALERTA_PRINTS_DIR = AWS_DIR / "prints"

def mostrar_readme(arquivo_readme, titulo):
    st.subheader(titulo)

    if arquivo_readme.exists():
        st.success(f"Arquivo encontrado: {arquivo_readme.relative_to(BASE_DIR)}")

        conteudo = arquivo_readme.read_text(encoding="utf-8", errors="ignore")
        st.markdown(conteudo)

        with open(arquivo_readme, "rb") as f:
            st.download_button(
                label=f"📥 Baixar {titulo}",
                data=f,
                file_name=arquivo_readme.name,
                mime="text/markdown",
                key=f"download_{titulo}_{arquivo_readme.parent.name}"
            )
    else:
        st.warning("README.md não encontrado.")
        st.code(str(arquivo_readme))


st.title("☁️ Fase 5 - AWS, Cloud e Alertas")

st.write("""
Nesta fase, foram trabalhados conceitos de Machine Learning aplicado à previsão
de rendimento de safra e análise de infraestrutura em nuvem com AWS.
""")

st.divider()

tab_alertas, tab_cap1 = st.tabs([
    "🚨 Alertas Fase 7",
    "📌 CAP1 - Machine Learning e AWS"
])


# =========================
# ALERTAS FASE 7
# =========================
with tab_alertas:
    st.header("🚨 Alertas AWS da Fase 7")

    st.write("""
    Esta seção apresenta o serviço de alertas desenvolvido para a Fase 7.
    O sistema lê dados de sensores agrícolas, verifica condições críticas e
    envia notificações por e-mail usando AWS SNS.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Serviço AWS", "SNS")
    col2.metric("Região", "sa-east-1")
    col3.metric("Entrega", "E-mail")

    st.divider()

    tab_resumo_alerta, tab_codigo_alerta, tab_dados_alerta, tab_evidencias_alerta, tab_readme_alerta = st.tabs([
        "📌 Resumo",
        "🐍 Código",
        "📊 Dados",
        "🖼️ Evidências",
        "📘 README"
    ])

    with tab_resumo_alerta:
        st.subheader("📌 Funcionamento do Alerta")

        st.write("""
        O módulo monitora os dados agrícolas e dispara alertas automáticos quando
        encontra condições críticas relacionadas ao solo, sensores ou manejo da irrigação.
        """)

        st.subheader("⚠️ Regras de alerta")

        st.markdown("""
        | Parâmetro | Regra crítica |
        |---|---|
        | pH | Abaixo de 4.5 ou acima de 7.5 |
        | NPK | N < 8, P < 80 ou K < 80 com bomba ligada |
        | Umidade | Abaixo de 20% |
        """)

        st.subheader("🔁 Fluxo da solução")

        st.code("""
dados_sensores.csv
        ↓
Script Python lê a última leitura
        ↓
Sistema verifica regras críticas
        ↓
Se houver problema, envia alerta via AWS SNS
        ↓
Funcionário recebe e-mail com ação recomendada
""", language="text")

        st.info("""
        O script também possui modo de simulação local caso as credenciais AWS
        não estejam configuradas no ambiente.
        """)

    with tab_codigo_alerta:
        st.subheader("🐍 Código do Serviço de Alerta")

        if ALERTA_SCRIPT.exists():
            st.success(f"Arquivo encontrado: {ALERTA_SCRIPT.relative_to(BASE_DIR)}")

            codigo = ALERTA_SCRIPT.read_text(encoding="utf-8", errors="ignore")
            st.code(codigo, language="python")

            with open(ALERTA_SCRIPT, "rb") as f:
                st.download_button(
                    label="📥 Baixar alerta_irrigacao_aws.py",
                    data=f,
                    file_name=ALERTA_SCRIPT.name,
                    mime="text/x-python"
                )
        else:
            st.warning("Script de alerta não encontrado.")
            st.code(str(ALERTA_SCRIPT))

    with tab_dados_alerta:
        st.subheader("📊 Dados dos Sensores")

        if ALERTA_CSV.exists():
            st.success(f"Arquivo encontrado: {ALERTA_CSV.relative_to(BASE_DIR)}")

            try:
                df_alerta = pd.read_csv(ALERTA_CSV)

                st.dataframe(df_alerta, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df_alerta.shape[0])
                col2.metric("Colunas", df_alerta.shape[1])
                col3.metric("Arquivo", ALERTA_CSV.name)

                st.subheader("Última leitura usada pelo alerta")
                st.dataframe(df_alerta.tail(1), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))

            with open(ALERTA_CSV, "rb") as f:
                st.download_button(
                    label="📥 Baixar dados_sensores.csv",
                    data=f,
                    file_name=ALERTA_CSV.name,
                    mime="text/csv"
                )
        else:
            st.warning("CSV dos sensores não encontrado.")
            st.code(str(ALERTA_CSV))

    with tab_evidencias_alerta:
        st.subheader("🖼️ Evidências AWS")

        if ALERTA_PRINTS_DIR.exists():
            imagens = sorted(
                list(ALERTA_PRINTS_DIR.glob("*.png")) +
                list(ALERTA_PRINTS_DIR.glob("*.jpg")) +
                list(ALERTA_PRINTS_DIR.glob("*.jpeg")) +
                list(ALERTA_PRINTS_DIR.glob("*.PNG")) +
                list(ALERTA_PRINTS_DIR.glob("*.JPG")) +
                list(ALERTA_PRINTS_DIR.glob("*.JPEG"))
            )

            if imagens:
                st.success(f"{len(imagens)} evidência(s) encontrada(s).")

                imagem_destaque = st.selectbox(
                    "Selecione uma evidência para visualizar",
                    imagens,
                    format_func=lambda x: x.name
                )

                st.image(
                    str(imagem_destaque),
                    caption=imagem_destaque.name,
                    use_container_width=True
                )

                st.divider()

                imagens_galeria = [img for img in imagens if img != imagem_destaque]

                if imagens_galeria:
                    st.divider()
                    st.subheader("📁 Outras evidências")

                    colunas = st.columns(2)

                    for index, imagem in enumerate(imagens_galeria):
                        with colunas[index % 2]:
                            st.image(
                                str(imagem),
                                caption=imagem.name,
                                use_container_width=True
                            )
            else:
                st.info("Nenhuma imagem encontrada na pasta de prints.")
        else:
            st.warning("Pasta de evidências não encontrada.")
            st.code(str(ALERTA_PRINTS_DIR))

    with tab_readme_alerta:
        st.subheader("📘 Documentação do Serviço de Alertas")

        if ALERTA_README.exists():
            conteudo = ALERTA_README.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)
        else:
            st.warning("README dos alertas não encontrado.")
            st.code(str(ALERTA_README))


# =========================
# CAP1
# =========================
with tab_cap1:
    st.header("📌 CAP1 - Previsão de Rendimento de Safra com Machine Learning")

    st.write("""
    O CAP1 apresenta uma solução para previsão de rendimento de safra usando dados
    climáticos e agrícolas. A atividade também inclui uma análise de custos na AWS
    para hospedar o modelo em uma API.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", "155")
    col2.metric("Culturas", "4")
    col3.metric("Modelos", "5")

    st.divider()

    tab_resumo, tab_dataset, tab_notebooks, tab_aws, tab_readme_cap1 = st.tabs([
        "📌 Resumo",
        "🌾 Dataset",
        "📓 Notebooks",
        "☁️ AWS",
        "📘 README",
    ])

    # =========================
    # RESUMO
    # =========================
    with tab_resumo:
        st.subheader("📌 Objetivo do Projeto")

        st.write("""
        O objetivo foi analisar uma base com condições de solo e clima relacionadas
        ao rendimento agrícola, explorando os dados, identificando padrões com
        clusterização e criando modelos supervisionados para prever o rendimento
        das safras.
        """)

        st.subheader("🧠 Modelos utilizados")

        st.markdown("""
        - Regressão Linear
        - Ridge Regression
        - Lasso Regression
        - Random Forest Regressor
        - Gradient Boosting Regressor
        """)

        st.subheader("🎥 Vídeos demonstrativos")

        st.markdown("""
        - [Entrega 1 - Machine Learning](https://youtu.be/rW4sRL_B4HM)
        - [Entrega 2 - AWS](https://youtu.be/Pp_OM9_DHxg)
        """)

    # =========================
    # DATASET
    # =========================
    with tab_dataset:
        st.subheader("🌾 Dataset crop_yield.csv")

        if CROP_YIELD.exists():
            st.success(f"Arquivo encontrado: {CROP_YIELD.relative_to(BASE_DIR)}")

            try:
                df = pd.read_csv(CROP_YIELD)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", CROP_YIELD.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))

            with open(CROP_YIELD, "rb") as f:
                st.download_button(
                    label="📥 Baixar crop_yield.csv",
                    data=f,
                    file_name=CROP_YIELD.name,
                    mime="text/csv"
                )
        else:
            st.warning("Arquivo crop_yield.csv não encontrado.")
            st.code(str(CROP_YIELD))

    # =========================
    # NOTEBOOKS
    # =========================
    with tab_notebooks:
        st.subheader("📓 Notebooks do Projeto")

        notebooks = [
            NOTEBOOK_EXECUTED,
            NOTEBOOK_PBL,
        ]

        for notebook in notebooks:
            if notebook.exists():
                st.success(f"Arquivo encontrado: {notebook.relative_to(BASE_DIR)}")

                with open(notebook, "rb") as f:
                    st.download_button(
                        label=f"📥 Baixar {notebook.name}",
                        data=f,
                        file_name=notebook.name,
                        mime="application/octet-stream"
                    )
            else:
                st.info(f"Notebook não encontrado: {notebook.name}")

        st.divider()

        st.subheader("🔧 Ir Além - Arduino")

        if IR_ALEM.exists():
            st.success(f"Arquivo encontrado: {IR_ALEM.relative_to(BASE_DIR)}")

            try:
                conteudo = IR_ALEM.read_text(encoding="utf-8", errors="ignore")
                st.code(conteudo, language="text")
            except Exception:
                st.write(f"✅ `{IR_ALEM.relative_to(BASE_DIR)}`")

            with open(IR_ALEM, "rb") as f:
                st.download_button(
                    label="📥 Baixar Ir Além",
                    data=f,
                    file_name=IR_ALEM.name,
                    mime="application/octet-stream"
                )
        else:
            st.info("Arquivo do Ir Além não encontrado.")

    # =========================
    # AWS
    # =========================
    with tab_aws:
        st.subheader("☁️ Entrega AWS - Estimativa de Custo")

        st.write("""
        A entrega de AWS estimou o custo para hospedar o modelo de Machine Learning
        em uma instância EC2, comparando as regiões São Paulo e Virgínia do Norte.
        """)

        col1, col2 = st.columns(2)
        col1.metric("São Paulo", "$18,62/mês")
        col2.metric("Virgínia", "$10,86/mês")

        st.info("""
        Apesar de Virgínia ser mais barata, São Paulo foi escolhida por motivos
        de LGPD, menor latência e soberania dos dados.
        """)

        if IMAGENS_DIR.exists():
            imagens = sorted(
                list(IMAGENS_DIR.glob("*.png")) +
                list(IMAGENS_DIR.glob("*.jpg")) +
                list(IMAGENS_DIR.glob("*.jpeg"))
            )

            if imagens:
                st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

                imagem_destaque = st.selectbox(
                    "Selecione uma imagem para visualizar",
                    imagens,
                    format_func=lambda x: x.name
                )

                st.image(
                    str(imagem_destaque),
                    caption=imagem_destaque.name,
                    use_container_width=True
                )

                st.divider()

                st.subheader("📁 Galeria AWS")

                colunas = st.columns(2)

                for index, imagem in enumerate(imagens):
                    with colunas[index % 2]:
                        st.image(
                            str(imagem),
                            caption=imagem.name,
                            use_container_width=True
                        )
            else:
                st.info("Nenhuma imagem encontrada em ATV5_2.")
        else:
            st.warning("Pasta ATV5_2 não encontrada.")
            st.code(str(IMAGENS_DIR))

        st.divider()

        st.subheader("📝 Roteiro do Vídeo")

        if ROTEIRO_VIDEO.exists():
            conteudo = ROTEIRO_VIDEO.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)
        else:
            st.info("ROTEIRO_VIDEO.md não encontrado.")

    # =========================
    # README CAP1
    # =========================
    with tab_readme_cap1:
        mostrar_readme(README_FILE, "📘 README do CAP1")

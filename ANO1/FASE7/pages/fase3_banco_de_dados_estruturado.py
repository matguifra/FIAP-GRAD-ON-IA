from pathlib import Path
import re
import base64

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]
FASE3_DIR = BASE_DIR / "assets" / "fase3"
CAP1_DIR = FASE3_DIR / "cap1"

# CAP1
README_CAP1 = CAP1_DIR / "README.md"

# CAP10
CAP10_DIR = FASE3_DIR / "cap10"
CAP10_NOTEBOOK = CAP10_DIR / "aprendizado-de-maquina.ipynb"
README_CAP10 = CAP10_DIR / "README.md"

# GS
GS_DIR = FASE3_DIR / "gs"

GS_PDF = GS_DIR / "global-solutions-burnout-predictor.pdf"
GS_CSV = GS_DIR / "dataset_burnout_adjusted_5000.csv"
GS_NOTEBOOK = GS_DIR / "burnout_predictor.ipynb"
GS_README = GS_DIR / "README.md"

DATA_DIR = CAP1_DIR / "data"
DOCS_DIR = CAP1_DIR / "docs"
SRC_DIR = CAP1_DIR / "src"

CSV_SENSORES = DATA_DIR / "dados_sensores.csv"
SQL_FILE = SRC_DIR / "consultas.sql"
README_FILE = CAP1_DIR / "README.md"
IR_ALEM_2 = CAP1_DIR / "ir-alem-2.ipynb"


st.title("🗄️ Fase 3 - Banco de Dados Estruturado")

st.write("""
Nesta fase, o foco foi estruturar um banco de dados Oracle para armazenar,
consultar e analisar dados agrícolas coletados por sensores. A etapa também
inclui entregas do Programa Ir Além com dashboard em Python e Machine Learning.
""")

st.divider()

tab_cap1, tab_cap10, tab_gs = st.tabs([
    "📌 CAP1",
    "📌 CAP10",
    "🌎 GS - Global Solution"
])


# =========================
# CAP1
# =========================
with tab_cap1:
    tab_oracle, tab_dados, tab_sql, tab_evidencias, tab_ir_alem, tab_readme_cap1 = st.tabs([
        "🗄️ Oracle",
        "📄 Dados",
        "💻 Consultas SQL",
        "🖼️ Evidências",
        "🚀 Ir Além",
        "📘 README"
    ])

    # =========================
    # ORACLE
    # =========================
    with tab_oracle:
        st.header("🗄️ Banco Oracle - SENSORES_FARMTECH")

        st.write("""
        A Fase 3 criou uma tabela relacional no Oracle para armazenar as leituras
        dos sensores agrícolas. Os dados importados vieram de um CSV gerado na fase
        anterior e foram usados em consultas de validação, filtros e estatísticas.
        """)

        col1, col2, col3 = st.columns(3)
        col1.metric("Tabela", "SENSORES_FARMTECH")
        col2.metric("Leituras", "48")
        col3.metric("Intervalo", "5 min")

        st.subheader("📌 Estrutura da tabela")

        st.code(
            """
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
""",
            language="sql"
        )

        st.subheader("🎥 Vídeo demonstrativo")
        st.video("https://youtu.be/Txpuv0JD0wU")

    # =========================
    # DADOS
    # =========================
    with tab_dados:
        st.header("📄 Base de Dados dos Sensores")

        st.write("""
        A base contém leituras simuladas de sensores agrícolas, incluindo pH do solo,
        umidade do solo, temperatura, sensação térmica, umidade do ar, nutrientes NPK
        e status da bomba.
        """)

        if CSV_SENSORES.exists():
            st.success(f"Arquivo encontrado: {CSV_SENSORES.relative_to(BASE_DIR)}")

            try:
                df = pd.read_csv(CSV_SENSORES)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", CSV_SENSORES.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

                colunas_numericas = df.select_dtypes(include="number").columns.tolist()

                if colunas_numericas:
                    coluna = st.selectbox(
                        "Selecione uma variável numérica para visualizar",
                        colunas_numericas
                    )

                    st.line_chart(df[coluna])

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))
        else:
            st.warning("Arquivo dados_sensores.csv não encontrado.")
            st.code(str(CSV_SENSORES))

    # =========================
    # SQL
    # =========================
    with tab_sql:
        st.header("💻 Consultas SQL")

        st.write("""
        As consultas SQL validam a importação dos dados, filtram leituras relevantes
        e calculam estatísticas como média, máximo e mínimo de umidade do solo.
        """)

        if SQL_FILE.exists():
            st.success(f"Arquivo encontrado: {SQL_FILE.relative_to(BASE_DIR)}")

            codigo_sql = SQL_FILE.read_text(encoding="utf-8", errors="ignore")
            st.code(codigo_sql, language="sql")

            with open(SQL_FILE, "rb") as f:
                st.download_button(
                    label="📥 Baixar consultas.sql",
                    data=f,
                    file_name=SQL_FILE.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo consultas.sql não encontrado.")
            st.code(str(SQL_FILE))

        st.subheader("📌 Consultas principais")

        st.markdown("""
        - `SELECT * FROM SENSORES_FARMTECH FETCH FIRST 20 ROWS ONLY`
        - `WHERE UMIDADE_SOLO > 70`
        - `ORDER BY PH_SOLO DESC`
        - `AVG`, `MAX` e `MIN` para análise estatística
        """)

    # =========================
    # EVIDÊNCIAS
    # =========================
    with tab_evidencias:
        st.header("🖼️ Evidências e Prints")

        st.write("""
        Esta aba reúne os prints do Oracle SQL Developer, importação dos dados,
        consultas SQL e resultados obtidos.
        """)

        if DOCS_DIR.exists():
            imagens = sorted(
                list(DOCS_DIR.glob("*.png")) +
                list(DOCS_DIR.glob("*.jpg")) +
                list(DOCS_DIR.glob("*.jpeg"))
            )

            if imagens:
                st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

                imagem_destaque = st.selectbox(
                    "Selecione uma imagem para visualizar em destaque",
                    imagens,
                    format_func=lambda x: x.name
                )

                st.image(
                    str(imagem_destaque),
                    caption=imagem_destaque.name,
                    use_container_width=True
                )

                st.divider()

                st.subheader("📁 Galeria completa")

                colunas = st.columns(3)

                for index, imagem in enumerate(imagens):
                    with colunas[index % 3]:
                        st.image(
                            str(imagem),
                            caption=imagem.name,
                            use_container_width=True
                        )
            else:
                st.info("Nenhuma imagem encontrada na pasta docs.")
        else:
            st.warning("Pasta docs não encontrada.")
            st.code(str(DOCS_DIR))

    # =========================
    # IR ALÉM
    # =========================
    with tab_ir_alem:
        st.header("🚀 Programa Ir Além")

        tab_ir1, tab_ir2 = st.tabs([
            "📊 Ir Além 1 - Dashboard",
            "🧠 Ir Além 2 - Machine Learning",
        ])

        with tab_ir1:
            st.subheader("📊 Ir Além 1 - Dashboard em Python")

            st.write("""
            O Ir Além 1 apresenta uma dashboard em Python para visualização das
            métricas principais dos sensores, gráficos interativos e recomendações
            de irrigação.
            """)

            st.video("https://youtu.be/J9iB4t9So8U")

            imagens_ir1 = [
                DOCS_DIR / "print1.png",
                DOCS_DIR / "print2.png",
                DOCS_DIR / "print3.png",
            ]

            for imagem in imagens_ir1:
                if imagem.exists():
                    st.image(str(imagem), caption=imagem.name, use_container_width=True)

        with tab_ir2:
            st.subheader("🧠 Ir Além 2 - Machine Learning no Agro")

            st.write("""
            O Ir Além 2 apresenta uma entrega com Machine Learning aplicada ao contexto
            agrícola, enviada em formato de notebook.
            """)

            st.video("https://youtu.be/pic7SCPDPn0")

            notebooks = sorted(CAP1_DIR.glob("*.ipynb"))

            if notebooks:
                st.write("Notebook(s) encontrado(s):")
                for notebook in notebooks:
                    st.write(f"✅ `{notebook.relative_to(BASE_DIR)}`")

                    with open(notebook, "rb") as f:
                        st.download_button(
                            label=f"📥 Baixar {notebook.name}",
                            data=f,
                            file_name=notebook.name,
                            mime="application/octet-stream"
                        )
            else:
                st.info("Nenhum notebook .ipynb encontrado na pasta da Fase 3.")

    # =========================
    # README CAP1
    # =========================
    with tab_readme_cap1:
        st.header("📘 README - CAP1")

        if README_CAP1.exists():
            st.success(f"Arquivo encontrado: {README_CAP1.relative_to(BASE_DIR)}")

            conteudo = README_CAP1.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)

            with open(README_CAP1, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP1",
                    data=f,
                    file_name=README_CAP1.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP1 não encontrado.")
            st.code(str(README_CAP1))

# =========================
# CAP10
# =========================
with tab_cap10:
    st.header("📌 CAP10 - Aprendizado de Máquina no Agronegócio")

    st.write("""
    O CAP10 trabalha com uma base de dados agrícola contendo características de solo,
    clima e o tipo de cultura recomendado para cada combinação de condições.
    A proposta foi realizar análise exploratória, análise descritiva e construir
    modelos preditivos para prever o melhor produto agrícola a ser cultivado.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Tipo de entrega", "Jupyter Notebook")
    col2.metric("Modelos exigidos", "5")
    col3.metric("Tema", "Classificação agrícola")

    st.divider()

    tab_cap10_resumo, tab_cap10_dataset, tab_cap10_notebook, tab_cap10_readme = st.tabs([
        "📌 Resumo",
        "🌱 Dataset",
        "📓 Notebook",
        "📘 README"
    ])

    # =========================
    # RESUMO
    # =========================
    with tab_cap10_resumo:
        st.subheader("📌 Proposta da Atividade")

        st.write("""
        A atividade consiste em analisar uma base de dados com informações de
        condições de solo e clima relacionadas ao tipo de produto agrícola.

        A partir dessa base, o grupo deveria:

        - realizar análise exploratória dos dados;
        - desenvolver uma análise descritiva com pelo menos cinco gráficos;
        - identificar o perfil ideal de solo e clima para as plantações;
        - comparar três culturas escolhidas com esse perfil ideal;
        - desenvolver cinco modelos preditivos com algoritmos diferentes;
        - avaliar os modelos com métricas adequadas ao problema.
        """)

        st.subheader("🎯 Objetivo")

        st.info("""
        Prever qual é o melhor produto agrícola a ser cultivado com base nas
        condições do solo e do clima.
        """)

    # =========================
    # DATASET
    # =========================
    with tab_cap10_dataset:
        st.subheader("🌱 Variáveis da Base de Dados")

        st.write("""
        A base utilizada foi o arquivo `produtos_agricolas.csv`, contendo variáveis
        relacionadas a nutrientes do solo, clima e cultura recomendada.
        """)

        st.markdown("""
        | Variável | Descrição |
        |---|---|
        | `N` | Quantidade de nitrogênio no solo |
        | `P` | Quantidade de fósforo no solo |
        | `K` | Quantidade de potássio no solo |
        | `temperature` | Temperatura média da região em °C |
        | `humidity` | Umidade média do ar |
        | `pH` | pH do solo |
        | `rainfall` | Precipitação em milímetros |
        | `label` | Tipo de cultura recomendada |
        """)

        st.subheader("🧠 Tipo de problema")

        st.write("""
        Como o objetivo é prever a cultura recomendada (`label`) a partir das
        demais variáveis, o problema é tratado como uma tarefa de **classificação
        supervisionada**.
        """)

    # =========================
    # NOTEBOOK
    # =========================
    with tab_cap10_notebook:
        st.subheader("📓 Notebook de Aprendizado de Máquina")

        if CAP10_NOTEBOOK.exists():
            st.success(f"Arquivo encontrado: {CAP10_NOTEBOOK.relative_to(BASE_DIR)}")

            st.write("""
            O notebook contém a análise exploratória, visualizações, comparação
            entre culturas e construção dos modelos preditivos solicitados.
            """)

            with open(CAP10_NOTEBOOK, "rb") as f:
                st.download_button(
                    label="📥 Baixar notebook",
                    data=f,
                    file_name=CAP10_NOTEBOOK.name,
                    mime="application/octet-stream"
                )

            st.info("""
            Para visualizar ou executar o notebook, abra o arquivo no Jupyter Notebook,
            JupyterLab, Google Colab ou VS Code com extensão de notebooks.
            """)

        else:
            st.warning("Notebook do CAP10 não encontrado.")
            st.code(str(CAP10_NOTEBOOK))

    # =========================
    # README CAP10
    # =========================
    with tab_cap10_readme:
        st.subheader("📘 README do CAP10")

        if README_CAP10.exists():
            st.success(f"Arquivo encontrado: {README_CAP10.relative_to(BASE_DIR)}")

            conteudo = README_CAP10.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)

            with open(README_CAP10, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP10",
                    data=f,
                    file_name=README_CAP10.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP10 não encontrado.")
            st.code(str(README_CAP10))

# =========================
# GS - GLOBAL SOLUTION
# =========================
with tab_gs:
    st.header("🌎 GS - Global Solutions 2025")

    st.write("""
    Esta seção reúne os materiais da Global Solutions 2025 — 2º semestre.
    A proposta consiste em um MVP com aplicação de Inteligência Artificial/Machine Learning,
    utilizando uma base de dados em CSV, um notebook Jupyter e um PDF de documentação.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Tipo", "MVP")
    col2.metric("Arquivos", "PDF + CSV + Notebook")
    col3.metric("Período", "2025/2")

    st.divider()

    tab_gs_resumo, tab_gs_pdf, tab_gs_dados, tab_gs_notebook, tab_gs_readme = st.tabs([
        "📌 Resumo",
        "📄 PDF",
        "📊 Dataset",
        "📓 Notebook",
        "📘 README"
    ])

    def mostrar_pdf(arquivo_pdf, label_download="📥 Baixar PDF"):
        if arquivo_pdf.exists():
            with open(arquivo_pdf, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")

            pdf_display = f"""
            <iframe
                src="data:application/pdf;base64,{base64_pdf}"
                width="100%"
                height="800px"
                type="application/pdf">
            </iframe>
            """

            st.markdown(pdf_display, unsafe_allow_html=True)

            with open(arquivo_pdf, "rb") as f:
                st.download_button(
                    label=label_download,
                    data=f,
                    file_name=arquivo_pdf.name,
                    mime="application/pdf"
                )
        else:
            st.warning("PDF não encontrado.")
            st.code(str(arquivo_pdf))
    

    # =========================
    # RESUMO
    # =========================
    with tab_gs_resumo:
        st.subheader("📌 Requisitos mínimos da GS")

        st.write("""
        Para concorrer à nota da Global Solution, o grupo deveria entregar:

        - MVP funcional;
        - aplicação de IA/Machine Learning;
        - coleta, tratamento e análise de dados;
        - demonstração prática em vídeo;
        - PDF único com link do vídeo, GitHub privado, integrantes, introdução,
          desenvolvimento, resultados esperados e conclusões;
        - explicações da solução, arquitetura, justificativas e códigos principais;
        - código e materiais operacionais e testados.
        """)

        st.subheader("🧠 Materiais integrados")

        st.info("""
        Esta aba integra os arquivos principais da Global Solution: PDF da entrega,
        base de dados em CSV e notebook Jupyter do projeto.
        """)

        if GS_README.exists():
            st.subheader("📘 README")

            conteudo_readme = GS_README.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo_readme)

    # =========================
    # PDF
    # =========================
    with tab_gs_pdf:
        st.subheader("📄 PDF da Global Solution")

        if GS_PDF.exists():
            st.success(f"Arquivo encontrado: {GS_PDF.relative_to(BASE_DIR)}")
            mostrar_pdf(GS_PDF, "📥 Baixar PDF da GS")
        else:
            st.warning("PDF da Global Solution não encontrado.")
            st.write("Pasta procurada:")
            st.code(str(GS_DIR))

            if GS_DIR.exists():
                st.write("Arquivos encontrados na pasta:")
                for arquivo in GS_DIR.iterdir():
                    st.write(f"✅ `{arquivo.name}`")

    # =========================
    # DATASET
    # =========================
    with tab_gs_dados:
        st.subheader("📊 Dataset - Burnout Predictor")

        if GS_CSV.exists():
            st.success(f"Arquivo encontrado: {GS_CSV.relative_to(BASE_DIR)}")

            try:
                df_gs = pd.read_csv(GS_CSV)

                st.dataframe(df_gs, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df_gs.shape[0])
                col2.metric("Colunas", df_gs.shape[1])
                col3.metric("Arquivo", GS_CSV.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df_gs.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))

                st.info("Exibindo conteúdo bruto:")
                conteudo = GS_CSV.read_text(encoding="utf-8", errors="ignore")
                st.code(conteudo[:5000], language="text")

            with open(GS_CSV, "rb") as f:
                st.download_button(
                    label="📥 Baixar dataset",
                    data=f,
                    file_name=GS_CSV.name,
                    mime="text/csv"
                )

        else:
            st.warning("Dataset da Global Solution não encontrado.")
            st.write("Pasta procurada:")
            st.code(str(GS_DIR))

            if GS_DIR.exists():
                st.write("Arquivos encontrados na pasta:")
                for arquivo in GS_DIR.iterdir():
                    st.write(f"✅ `{arquivo.name}`")

    # =========================
    # NOTEBOOK
    # =========================
    with tab_gs_notebook:
        st.subheader("📓 Notebook - Burnout Predictor")

        if GS_NOTEBOOK.exists():
            st.success(f"Arquivo encontrado: {GS_NOTEBOOK.relative_to(BASE_DIR)}")

            st.write("""
            O notebook reúne as etapas de análise, tratamento dos dados,
            modelagem e avaliação relacionadas ao projeto da Global Solution.
            """)

            with open(GS_NOTEBOOK, "rb") as f:
                st.download_button(
                    label="📥 Baixar notebook",
                    data=f,
                    file_name=GS_NOTEBOOK.name,
                    mime="application/octet-stream"
                )

            st.info("""
            Para visualizar ou executar o notebook, abra o arquivo no Jupyter Notebook,
            Google Colab ou VS Code com suporte a notebooks.
            """)

        else:
            st.warning("Notebook da Global Solution não encontrado.")
            st.write("Pasta procurada:")
            st.code(str(GS_DIR))

            if GS_DIR.exists():
                st.write("Arquivos encontrados na pasta:")
                for arquivo in GS_DIR.iterdir():
                    st.write(f"✅ `{arquivo.name}`")

    # =========================
    # README GS
    # =========================
    with tab_gs_readme:
        st.subheader("📘 README da Global Solution")

        if GS_README.exists():
            st.success(f"Arquivo encontrado: {GS_README.relative_to(BASE_DIR)}")

            conteudo = GS_README.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)

            with open(GS_README, "rb") as f:
                st.download_button(
                    label="📥 Baixar README da GS",
                    data=f,
                    file_name=GS_README.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md da Global Solution não encontrado.")
            st.code(str(GS_README))
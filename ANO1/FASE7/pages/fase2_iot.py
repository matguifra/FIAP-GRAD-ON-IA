from pathlib import Path
import re
import pandas as pd

import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]
FASE2_DIR = BASE_DIR / "assets" / "fase2"

ESP32_DIR = FASE2_DIR / "cap1" / "ESP32"
CODIGO_ESP32 = ESP32_DIR / "codigo_esp32.ino"
README_ESP32 = ESP32_DIR / "README.md"
GALERIA_DIR = ESP32_DIR / "assets"

DATA_SCIENCE_DIR = FASE2_DIR / "cap1" / "data_science"

ARQUIVO_RDATA = DATA_SCIENCE_DIR / ".RData"
ARQUIVO_RHISTORY = DATA_SCIENCE_DIR / ".Rhistory"
ARQUIVO_DADOS_SENSORES = DATA_SCIENCE_DIR / "dados_sensores.csv"
ARQUIVO_MODELO_RDS = DATA_SCIENCE_DIR / "modelo_bomba.rds"

CAP6_DIR = FASE2_DIR / "cap6"

CAP6_APP = CAP6_DIR / "app.py"
CAP6_ORACLE_CONFIG = CAP6_DIR / "referencia de configuracao Oracle"

README_CAP6 = CAP6_DIR / "README.md"

CAP7_DIR = FASE2_DIR / "cap7"

CAP7_SCRIPT_R = CAP7_DIR / "script_novo.R"
CAP7_EXCEL = CAP7_DIR / "tabela_formatada.xlsx"

README_CAP7 = CAP7_DIR / "README.md"

st.title("📡 Fase 2 - IoT, Sensores e ESP32")

st.write("""
Nesta seção estão os materiais da Fase 2 relacionados à aplicação com ESP32,
sensores, links de apoio e evidências visuais do projeto.
""")

st.divider()

tab_cap1, tab_cap6, tab_cap7 = st.tabs([
    "📌 CAP1 - ESP32 e Sensores",
    "☁️ CAP6 - ORACLE",
    "📊 CAP7 - Data Science R"
])

# =========================
# ABA CAP1
# =========================

with tab_cap1:
    st.header("📌 CAP1 - ESP32, Sensores e Data Science")

    st.write("""
    Este capítulo reúne os materiais principais da Fase 2, incluindo links do projeto,
    código do ESP32, imagens da montagem/simulação e arquivos de Data Science.
    """)

    tab_links, tab_esp32, tab_galeria, tab_data_science, tab_readme_esp32 = st.tabs([
        "🔗 Links",
        "🤖 Código ESP32",
        "🖼️ Galeria",
        "📊 Data Science",
        "📘 README"
    ])

    # aqui dentro ficam seus blocos antigos:
    # with tab_links:
    # with tab_esp32:
    # with tab_galeria:
    # with tab_data_science:

# =========================
# ABA LINKS
# =========================
with tab_links:
    st.header("🔗 Links do Projeto")

    st.subheader("🎥 Vídeo de demonstração")
    st.video("https://www.youtube.com/watch?v=ZCE25_D37qg")

    st.divider()

    st.subheader("🖼️ Imagem do projeto")
    st.image(
        "https://i.imgur.com/hiLPUVm.png",
        caption="Imagem demonstrativa do projeto ESP32",
        use_container_width=True
    )

    st.divider()

    st.subheader("📎 Links adicionais")

    links_files = list(FASE2_DIR.rglob("links.txt"))

if not links_files:
    st.warning("Nenhum arquivo links.txt encontrado dentro de assets/fase2.")
    st.code(str(FASE2_DIR))
else:
    links_file = links_files[0]

    st.success(f"Arquivo encontrado: {links_file.relative_to(BASE_DIR)}")

    conteudo = links_file.read_text(encoding="utf-8", errors="ignore")
    links = re.findall(r"https?://[^\s]+", conteudo)

    if links:
        st.subheader("Links encontrados")

        for i, link in enumerate(links, start=1):
            st.markdown(f"{i}. [{link}]({link})")
    else:
        st.info("Nenhum link no formato http/https foi encontrado.")

    with st.expander("Ver conteúdo completo do links.txt"):
        st.code(conteudo, language="text")


# =========================
# ABA ESP32
# =========================
with tab_esp32:
    st.header("🤖 Código ESP32")

    st.write("""
    Esta aba apresenta o código utilizado no ESP32 para leitura de sensores,
    controle de lógica do sistema e apoio à automação agrícola.
    """)

    if CODIGO_ESP32.exists():
        st.success(f"Arquivo encontrado: {CODIGO_ESP32.relative_to(BASE_DIR)}")

        codigo = CODIGO_ESP32.read_text(encoding="utf-8", errors="ignore")

        st.subheader("📄 codigo_esp32.ino")
        st.code(codigo, language="cpp")

        st.info("Este arquivo deve ser aberto na Arduino IDE, PlatformIO ou simulador como Wokwi.")

        with open(CODIGO_ESP32, "rb") as f:
            st.download_button(
                label="📥 Baixar código ESP32",
                data=f,
                file_name=CODIGO_ESP32.name,
                mime="text/plain"
            )
    else:
        st.warning("Arquivo codigo_esp32.ino não encontrado.")
        st.code(str(CODIGO_ESP32))


# =========================
# ABA README ESP32
# =========================
with tab_readme_esp32:
    st.header("📘 README - CAP1 ESP32")

    st.write("""
    Esta aba apresenta a documentação do CAP1 da Fase 2, relacionada ao projeto
    com ESP32, sensores, simulação e integração com dados agrícolas.
    """)

    if README_ESP32.exists():
        st.success(f"Arquivo encontrado: {README_ESP32.relative_to(BASE_DIR)}")

        conteudo_readme = README_ESP32.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        st.markdown(conteudo_readme)

        with open(README_ESP32, "rb") as f:
            st.download_button(
                label="📥 Baixar README do CAP1 ESP32",
                data=f,
                file_name=README_ESP32.name,
                mime="text/markdown"
            )
    else:
        st.warning("README.md do CAP1 ESP32 não encontrado.")
        st.code(str(README_ESP32))


# =========================
# ABA GALERIA
# =========================
with tab_galeria:
    st.header("🖼️ Galeria do Projeto ESP32")

    st.write("""
    Esta galeria reúne as imagens do projeto, como montagem do circuito,
    simulação, sensores, dashboard ou evidências visuais da aplicação.
    """)

    if not GALERIA_DIR.exists():
        st.warning("Pasta de galeria não encontrada.")
        st.code(str(GALERIA_DIR))
    else:
        imagens = sorted(GALERIA_DIR.glob("*.png"))

        if not imagens:
            st.info("Nenhuma imagem PNG encontrada na pasta de galeria.")
        else:
            st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

            # Imagem em destaque
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

            st.subheader("📁 Todas as imagens")

            # Galeria em grade com 3 colunas
            colunas = st.columns(3)

            for index, imagem in enumerate(imagens):
                with colunas[index % 3]:
                    st.image(
                        str(imagem),
                        caption=imagem.name,
                        use_container_width=True
                    )

                    with open(imagem, "rb") as f:
                        st.download_button(
                            label="Baixar",
                            data=f,
                            file_name=imagem.name,
                            mime="image/png",
                            key=f"download_{imagem.name}"
                        )

# =========================
# ABA DATA SCIENCE
# =========================
with tab_data_science:
    st.header("📊 Data Science - Sensores e Modelo da Bomba")

    st.write("""
    Esta aba apresenta os arquivos de Data Science usados na Fase 2,
    incluindo dados de sensores, histórico do R e arquivos do modelo treinado.
    """)

    tab_rdata, tab_rhistory, tab_dados, tab_modelo = st.tabs([
        "📦 .RData",
        "📜 .Rhistory",
        "🌡️ dados_sensores",
        "🧠 modelo_bomba.rds"
    ])

    # -------------------------
    # .RData
    # -------------------------
    with tab_rdata:
        st.subheader("📦 Arquivo .RData")

        if ARQUIVO_RDATA.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_RDATA.relative_to(BASE_DIR)}")

            st.info("""
            O arquivo `.RData` armazena objetos do ambiente R, como datasets,
            variáveis, modelos ou resultados salvos durante a análise.
            """)

            st.write("Tamanho do arquivo:")
            st.code(f"{ARQUIVO_RDATA.stat().st_size / 1024:.2f} KB")

            with open(ARQUIVO_RDATA, "rb") as f:
                st.download_button(
                    label="📥 Baixar .RData",
                    data=f,
                    file_name=ARQUIVO_RDATA.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Arquivo .RData não encontrado.")
            st.code(str(ARQUIVO_RDATA))

    # -------------------------
    # .Rhistory
    # -------------------------
    with tab_rhistory:
        st.subheader("📜 Histórico de comandos R")

        if ARQUIVO_RHISTORY.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_RHISTORY.relative_to(BASE_DIR)}")

            conteudo = ARQUIVO_RHISTORY.read_text(encoding="utf-8", errors="ignore")

            if conteudo.strip():
                st.code(conteudo, language="r")
            else:
                st.info("O arquivo .Rhistory está vazio.")

            with open(ARQUIVO_RHISTORY, "rb") as f:
                st.download_button(
                    label="📥 Baixar .Rhistory",
                    data=f,
                    file_name=ARQUIVO_RHISTORY.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo .Rhistory não encontrado.")
            st.code(str(ARQUIVO_RHISTORY))

    # -------------------------
    # dados_sensores
    # -------------------------
    with tab_dados:
        st.subheader("🌡️ Dados dos Sensores")

        if ARQUIVO_DADOS_SENSORES.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_DADOS_SENSORES.relative_to(BASE_DIR)}")

            try:
                df = pd.read_csv(ARQUIVO_DADOS_SENSORES)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", ARQUIVO_DADOS_SENSORES.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o arquivo como CSV.")
                st.code(str(erro))

                st.info("Exibindo conteúdo bruto:")
                conteudo = ARQUIVO_DADOS_SENSORES.read_text(encoding="utf-8", errors="ignore")
                st.code(conteudo[:5000], language="text")

            with open(ARQUIVO_DADOS_SENSORES, "rb") as f:
                st.download_button(
                    label="📥 Baixar dados_sensores",
                    data=f,
                    file_name=ARQUIVO_DADOS_SENSORES.name,
                    mime="text/csv"
                )
        else:
            st.warning("Arquivo dados_sensores não encontrado.")
            st.code(str(ARQUIVO_DADOS_SENSORES))

    # -------------------------
    # modelo_bomba.rds
    # -------------------------

    with tab_modelo:
        st.subheader("🧠 Modelo da Bomba - RDS")

        if ARQUIVO_MODELO_RDS.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_MODELO_RDS.relative_to(BASE_DIR)}")

            st.info("""
            O arquivo `.rds` é um objeto salvo pelo R. Ele pode conter um modelo treinado,
            neste caso relacionado à lógica de acionamento/previsão da bomba.
            """)

            st.write("Tamanho do arquivo:")
            st.code(f"{ARQUIVO_MODELO_RDS.stat().st_size / 1024:.2f} KB")

            st.write("Exemplo de comando para carregar no R:")
            st.code(
                'modelo <- readRDS("modelo_bomba.rds")',
                language="r"
            )

            with open(ARQUIVO_MODELO_RDS, "rb") as f:
                st.download_button(
                    label="📥 Baixar modelo_bomba.rds",
                    data=f,
                    file_name=ARQUIVO_MODELO_RDS.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Arquivo modelo_bomba.rds não encontrado.")
            st.code(str(ARQUIVO_MODELO_RDS))

with tab_cap6:
    st.header("☁️ CAP6 - Python, Oracle e Gestão de Colheita")

    st.write("""
    O CAP6 apresenta um sistema em Python para gestão de operações de colheita
    de cana-de-açúcar. A aplicação permite cadastrar talhões, registrar operações,
    calcular alertas de perda e salvar os dados em relatório, JSON ou banco Oracle.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Tema", "Colheita")
    col2.metric("Banco", "Oracle")
    col3.metric("Alerta", "Perda (%)")

    st.divider()

    tab_cap6_resumo, tab_cap6_codigo, tab_cap6_oracle, tab_cap6_readme = st.tabs([
        "📌 Resumo",
        "🐍 Código Python",
        "🗄️ Configuração Oracle",
        "📘 README"
    ])

    # =========================
    # RESUMO
    # =========================
    with tab_cap6_resumo:
        st.subheader("📌 Funcionalidades do Sistema")

        st.write("""
        O sistema trabalha com dois conjuntos principais de dados:

        - **Talhões:** áreas agrícolas cadastradas com ID, nome e área.
        - **Operações:** registros de colheita com data, peso colhido, perda e alerta.

        A lógica de alerta considera a porcentagem de perda:

        - **Baixa:** menor que 8%
        - **Média:** entre 8% e 15%
        - **Alta:** maior que 15%
        """)

        st.subheader("▶️ Como executar")

        if CAP6_APP.exists():
            st.code(
                f"python {CAP6_APP.relative_to(BASE_DIR)}",
                language="bash"
            )
        else:
            st.warning("Arquivo app.py do CAP6 não encontrado.")
            st.code(str(CAP6_APP))

        st.info("""
        Antes de usar a integração com Oracle, é necessário instalar a biblioteca:

        pip install oracledb
        """)

    # =========================
    # CÓDIGO PYTHON
    # =========================
    with tab_cap6_codigo:
        st.subheader("🐍 Código principal - app.py")

        if CAP6_APP.exists():
            st.success(f"Arquivo encontrado: {CAP6_APP.relative_to(BASE_DIR)}")

            codigo = CAP6_APP.read_text(encoding="utf-8", errors="ignore")

            st.code(codigo, language="python")

            with open(CAP6_APP, "rb") as f:
                st.download_button(
                    label="📥 Baixar app.py",
                    data=f,
                    file_name=CAP6_APP.name,
                    mime="text/x-python"
                )
        else:
            st.warning("Arquivo app.py não encontrado.")
            st.code(str(CAP6_APP))

    # =========================
    # CONFIGURAÇÃO ORACLE
    # =========================
    with tab_cap6_oracle:
        st.subheader("🗄️ Referência de Configuração Oracle")

        st.write("""
        A integração com Oracle depende das variáveis de ambiente abaixo:

        - `ORA_USER`
        - `ORA_PASS`
        - `ORA_DSN`
        """)

        if CAP6_ORACLE_CONFIG.exists():
            st.success(f"Arquivo encontrado: {CAP6_ORACLE_CONFIG.relative_to(BASE_DIR)}")

            conteudo = CAP6_ORACLE_CONFIG.read_text(encoding="utf-8", errors="ignore")
            st.code(conteudo, language="text")

            with open(CAP6_ORACLE_CONFIG, "rb") as f:
                st.download_button(
                    label="📥 Baixar referência Oracle",
                    data=f,
                    file_name=CAP6_ORACLE_CONFIG.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo de referência Oracle não encontrado.")
            st.code(str(CAP6_ORACLE_CONFIG))

    # =========================
    # README CAP6
    # =========================
    with tab_cap6_readme:
        st.subheader("📘 README do CAP6")

        if README_CAP6.exists():
            st.success(f"Arquivo encontrado: {README_CAP6.relative_to(BASE_DIR)}")

            conteudo = README_CAP6.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)

            with open(README_CAP6, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP6",
                    data=f,
                    file_name=README_CAP6.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP6 não encontrado.")
            st.code(str(README_CAP6))

with tab_cap7:
    st.header("📊 CAP7 - Estatística com R e Base Excel")

    st.write("""
    O CAP7 trabalha com uma base de dados em Excel relacionada ao agronegócio
    e uma análise exploratória feita em R. A proposta envolve variáveis
    quantitativas e qualitativas, medidas estatísticas e visualizações gráficas.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Base mínima", "30 linhas")
    col2.metric("Colunas exigidas", "4")
    col3.metric("Ferramenta", "R + Excel")

    st.divider()

    tab_cap7_resumo, tab_cap7_excel, tab_cap7_r, tab_cap7_readme = st.tabs([
        "📌 Resumo",
        "📄 Base Excel",
        "📊 Código R",
        "📘 README"
    ])
    # =========================
    # RESUMO
    # =========================
    with tab_cap7_resumo:
        st.subheader("📌 Requisitos do CAP7")

        st.write("""
        Nesta atividade, foi necessário pesquisar dados públicos relacionados
        ao agronegócio e criar uma base em Excel contendo pelo menos:

        - Uma variável quantitativa discreta
        - Uma variável quantitativa contínua
        - Uma variável qualitativa nominal
        - Uma variável qualitativa ordinal

        Em seguida, foi feita uma análise exploratória em R com:

        - Medidas de tendência central
        - Medidas de dispersão
        - Medidas separatrizes
        - Análise gráfica de variável quantitativa
        - Análise gráfica de variável qualitativa
        """)

        st.subheader("📚 Fontes sugeridas no enunciado")

        st.markdown("""
        - [CONAB](https://www.conab.gov.br/)
        - [IBGE](https://www.ibge.gov.br/)
        - [MAPA](https://www.gov.br/agricultura/pt-br)
        - [Embrapa](https://www.embrapa.br/)
        - [INPE](https://www.gov.br/inpe/pt-br)
        - [CNA Brasil](https://www.cnabrasil.org.br/)
        """)

        st.subheader("▶️ Como executar o script R")

        if CAP7_SCRIPT_R.exists():
            st.code(
                f"Rscript {CAP7_SCRIPT_R.relative_to(BASE_DIR)}",
                language="bash"
            )
        else:
            st.warning("Arquivo R do CAP7 não encontrado.")
            st.code(str(CAP7_SCRIPT_R))

    # =========================
    # EXCEL
    # =========================
    with tab_cap7_excel:
        st.subheader("📄 Base de Dados em Excel")

        if CAP7_EXCEL.exists():
            st.success(f"Arquivo encontrado: {CAP7_EXCEL.relative_to(BASE_DIR)}")

            try:
                df_excel = pd.read_excel(CAP7_EXCEL)

                st.dataframe(df_excel, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df_excel.shape[0])
                col2.metric("Colunas", df_excel.shape[1])
                col3.metric("Arquivo", CAP7_EXCEL.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df_excel.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o Excel.")
                st.code(str(erro))

            with open(CAP7_EXCEL, "rb") as f:
                st.download_button(
                    label="📥 Baixar base Excel",
                    data=f,
                    file_name=CAP7_EXCEL.name,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.warning("Arquivo Excel do CAP7 não encontrado.")
            st.code(str(CAP7_EXCEL))

    # =========================
    # CÓDIGO R
    # =========================
    with tab_cap7_r:
        st.subheader("📊 Script R - Análise Exploratória")

        if CAP7_SCRIPT_R.exists():
            st.success(f"Arquivo encontrado: {CAP7_SCRIPT_R.relative_to(BASE_DIR)}")

            codigo_r = CAP7_SCRIPT_R.read_text(encoding="utf-8", errors="ignore")

            st.code(codigo_r, language="r")

            with open(CAP7_SCRIPT_R, "rb") as f:
                st.download_button(
                    label="📥 Baixar script R",
                    data=f,
                    file_name=CAP7_SCRIPT_R.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo R do CAP7 não encontrado.")
            st.code(str(CAP7_SCRIPT_R))

    # =========================
    # README CAP7
    # =========================
    with tab_cap7_readme:
        st.subheader("📘 README do CAP7")

        if README_CAP7.exists():
            st.success(f"Arquivo encontrado: {README_CAP7.relative_to(BASE_DIR)}")

            conteudo = README_CAP7.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)

            with open(README_CAP7, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP7",
                    data=f,
                    file_name=README_CAP7.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP7 não encontrado.")
            st.code(str(README_CAP7))

st.divider()

st.header("📌 Integração com a Fase 7")

st.write("""
Esta página integra os links, o código ESP32 e as evidências visuais da Fase 2
dentro do dashboard central da Fase 7, mantendo os arquivos organizados dentro
da pasta assets.
""")
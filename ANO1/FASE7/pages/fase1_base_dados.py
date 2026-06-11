import base64
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]

FASE1_CAP1_DIR = BASE_DIR / "assets" / "fase1" / "cap1"
FASE1_CAP2_DIR = BASE_DIR / "assets" / "fase1" / "cap2"

arquivo_python = FASE1_CAP1_DIR / "lavouras.py"
arquivo_r = FASE1_CAP1_DIR / "lavouras.R"
arquivo_pdf = FASE1_CAP2_DIR / "relatorio.pdf"
arquivo_tm = FASE1_CAP2_DIR / "project.tm"

arquivo_readme_cap1 = FASE1_CAP1_DIR / "README.md"
arquivo_readme_cap2 = FASE1_CAP2_DIR / "README.md"


st.set_page_config(
    page_title="Fase 1 - Base de Dados",
    page_icon="🌾",
    layout="wide"
)


def mostrar_codigo(arquivo, linguagem="python"):
    if arquivo.exists():
        codigo = arquivo.read_text(encoding="utf-8", errors="ignore")
        st.code(codigo, language=linguagem)
    else:
        st.warning(f"Arquivo não encontrado: {arquivo}")


def mostrar_pdf(arquivo_pdf):
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
                label="📥 Baixar relatório em PDF",
                data=f,
                file_name=arquivo_pdf.name,
                mime="application/pdf"
            )
    else:
        st.warning("PDF do CAP2 não encontrado.")
        st.code(str(arquivo_pdf))


def mostrar_markdown(arquivo_md):
    if arquivo_md.exists():
        conteudo = arquivo_md.read_text(encoding="utf-8", errors="ignore")
        st.markdown(conteudo)
    else:
        st.warning("README não encontrado.")
        st.code(str(arquivo_md))


st.title("🌾 Fase 1 - Base de Dados, Lavouras e Introdução à IA")

st.write("""
Nesta fase, foram desenvolvidos os primeiros recursos do projeto FarmTech,
incluindo cálculos de área de plantio, manejo de insumos, análise estatística
em R e uma introdução ao reconhecimento de imagens com Teachable Machine.
""")

st.divider()

tab_cap1, tab_cap2 = st.tabs([
    "CAP1 - Lavouras e Estatística",
    "CAP2 - Teachable Machine"
])


# =========================
# CAP1
# =========================
with tab_cap1:
    st.header("CAP1 - Sistema de Gestão de Lavouras")

    st.write("""
    No CAP1, foi desenvolvido um sistema para cadastrar lavouras, calcular área,
    estimar consumo de nutrientes e organizar os dados para análise estatística.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Linguagem principal", "Python")
        st.metric("Tipo de sistema", "CRUD agrícola")

    with col2:
        st.metric("Análise estatística", "R")
        st.metric("Dados calculados", "Área, NPK e água")

    st.divider()

    tab_cap1_resumo, tab_cap1_python, tab_cap1_r, tab_cap1_readme = st.tabs([
        "📌 Resumo",
        "🐍 Código Python",
        "📊 Código R",
        "📘 README"
    ])

    with tab_cap1_resumo:
        st.subheader("📌 Resumo do CAP1")

        st.write("""
        Este capítulo apresenta a primeira aplicação agrícola do projeto FarmTech.
        A proposta foi desenvolver um sistema em Python para gerenciamento de
        lavouras, cálculo de área de plantio e manejo de insumos.
        """)

        st.markdown("""
        **Principais entregas:**

        - Aplicação em Python com menu interativo;
        - Cadastro e gerenciamento de dados agrícolas;
        - Cálculo de área de plantio;
        - Cálculo de manejo de insumos;
        - Organização dos dados em vetores;
        - Análise estatística básica em R;
        - Integração dos arquivos à dashboard da Fase 7.
        """)

    with tab_cap1_python:
        st.subheader("🐍 Código Python - Sistema de Lavouras")

        if arquivo_python.exists():
            st.success(f"Encontrado: {arquivo_python.relative_to(BASE_DIR)}")
            mostrar_codigo(arquivo_python, "python")

            st.write("Comando para executar:")
            st.code(
                f"python {arquivo_python.relative_to(BASE_DIR)}",
                language="bash"
            )
        else:
            st.warning("Arquivo Python do CAP1 não encontrado.")
            st.code(str(arquivo_python))

    with tab_cap1_r:
        st.subheader("📊 Código R - Análise Estatística")

        if arquivo_r.exists():
            st.success(f"Encontrado: {arquivo_r.relative_to(BASE_DIR)}")
            mostrar_codigo(arquivo_r, "r")

            st.write("Comando para executar:")
            st.code(
                f"Rscript {arquivo_r.relative_to(BASE_DIR)}",
                language="bash"
            )
        else:
            st.warning("Arquivo R do CAP1 não encontrado.")
            st.code(str(arquivo_r))

    with tab_cap1_readme:
        st.subheader("📘 README do CAP1")

        if arquivo_readme_cap1.exists():
            st.success(f"Encontrado: {arquivo_readme_cap1.relative_to(BASE_DIR)}")
            mostrar_markdown(arquivo_readme_cap1)

            with open(arquivo_readme_cap1, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP1",
                    data=f,
                    file_name=arquivo_readme_cap1.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP1 não encontrado.")
            st.code(str(arquivo_readme_cap1))


# =========================
# CAP2
# =========================
with tab_cap2:
    st.header("CAP2 - Reconhecimento de Imagens com Teachable Machine")

    subtab_visao_geral, subtab_readme = st.tabs([
        "📌 Visão Geral",
        "📘 README"
    ])

    with subtab_visao_geral:
        st.write("""
        No CAP2, foi desenvolvido um modelo de reconhecimento de imagens utilizando
        o Teachable Machine do Google. O modelo classifica imagens em três categorias:
        panelas, espátulas e assadeiras.
        """)

        col1, col2, col3 = st.columns(3)

        col1.metric("Classes", "3")
        col2.metric("Epochs", "50")
        col3.metric("Learning rate", "0.001")

        st.divider()

        st.subheader("📄 Relatório do Projeto")

        if arquivo_pdf.exists():
            st.success(f"Encontrado: {arquivo_pdf.relative_to(BASE_DIR)}")
            mostrar_pdf(arquivo_pdf)
        else:
            st.warning("Relatório PDF não encontrado.")
            st.code(str(arquivo_pdf))

        st.divider()

        st.subheader("📦 Arquivo do Modelo Teachable Machine")

        if arquivo_tm.exists():
            st.success(f"Encontrado: {arquivo_tm.relative_to(BASE_DIR)}")

            with open(arquivo_tm, "rb") as f:
                st.download_button(
                    label="📥 Baixar arquivo project.tm",
                    data=f,
                    file_name=arquivo_tm.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Arquivo project.tm não encontrado.")
            st.code(str(arquivo_tm))

    with subtab_readme:
        st.subheader("📘 README do CAP2")

        if arquivo_readme_cap2.exists():
            st.success(f"Encontrado: {arquivo_readme_cap2.relative_to(BASE_DIR)}")
            mostrar_markdown(arquivo_readme_cap2)

            with open(arquivo_readme_cap2, "rb") as f:
                st.download_button(
                    label="📥 Baixar README do CAP2",
                    data=f,
                    file_name=arquivo_readme_cap2.name,
                    mime="text/markdown"
                )
        else:
            st.warning("README.md do CAP2 não encontrado.")
            st.code(str(arquivo_readme_cap2))


st.divider()

st.header("Integração com a Fase 7")

st.write("""
Esta página integra os materiais da Fase 1 dentro da dashboard central da Fase 7.
O CAP1 apresenta a base agrícola com Python e R, enquanto o CAP2 apresenta a
primeira experiência com reconhecimento de imagens.
""")
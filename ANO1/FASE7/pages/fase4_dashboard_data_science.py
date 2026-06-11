import os
import sys
import runpy
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]

# CAP1 - Dashboard original da Fase 4
CAP1_DIR = BASE_DIR / "assets" / "fase4" / "cap1"

FASE4_HOME = CAP1_DIR / "fase4_home.py"
FASE4_EXPLORACAO = CAP1_DIR / "fase4_exploracao.py"
FASE4_MODELAGEM = CAP1_DIR / "fase4_modelagem.py"
README_CAP1 = CAP1_DIR / "README.md"

# CAP3 - Seeds Classification ML
CAP3_DIR = BASE_DIR / "assets" / "fase4" / "cap3"
CAP3_NOTEBOOK = CAP3_DIR / "seeds_classification_ml.ipynb"
README_CAP3 = CAP3_DIR / "README.md"




st.title("📊 Fase 4 - Dashboard e Data Science")

st.write("""
Nesta fase, foram desenvolvidas soluções com Streamlit e Machine Learning,
incluindo dashboard interativo para análise agrícola e modelos de classificação
aplicados ao contexto do agronegócio.
""")

st.divider()

tab_cap1, tab_cap3 = st.tabs([
    "📌 CAP1 - Dashboard Agrícola",
    "🌾 CAP3 - Classificação de Sementes"
])


def executar_pagina(arquivo):
    if not arquivo.exists():
        st.warning("Arquivo não encontrado.")
        st.code(str(arquivo))
        return

    if str(CAP1_DIR) not in sys.path:
        sys.path.insert(0, str(CAP1_DIR))

    pasta_atual = Path.cwd()

    try:
        os.chdir(CAP1_DIR)

        # Evita conflito caso a página antiga tenha st.set_page_config()
        st.set_page_config = lambda *args, **kwargs: None

        runpy.run_path(str(arquivo), run_name="__main__")

    finally:
        os.chdir(pasta_atual)

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


# =========================
# CAP1
# =========================
with tab_cap1:
    st.header("📌 CAP1 - Dashboard Agrícola com Streamlit")

    st.write("""
    O CAP1 reúne a aplicação original em Streamlit da Fase 4, com tela inicial,
    exploração de dados e modelagem preditiva.
    """)

    tab_home, tab_exploracao, tab_modelagem, tab_readme_cap1 = st.tabs([
        "🏠 Home",
        "🔎 Exploração",
        "🤖 Modelagem e Previsão",
        "📘 README"
    ])

    with tab_home:
        executar_pagina(FASE4_HOME)

    with tab_exploracao:
        executar_pagina(FASE4_EXPLORACAO)

    with tab_modelagem:
        executar_pagina(FASE4_MODELAGEM)

    with tab_readme_cap1:
        mostrar_readme(README_CAP1, "📘 README do CAP1")


# =========================
# CAP3
# =========================
with tab_cap3:
    st.header("🌾 CAP3 - Classificação de Sementes com Machine Learning")

    st.write("""
    O CAP3 aplica a metodologia CRISP-DM para desenvolver modelos de Machine Learning
    capazes de classificar variedades de grãos de trigo com base em características físicas.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Dataset", "Seeds - UCI")
    col2.metric("Amostras", "210")
    col3.metric("Classes", "3")

    st.divider()

    tab_cap3_resumo, tab_cap3_notebook, tab_readme_cap3 = st.tabs([
        "📌 Resumo",
        "📓 Notebook",
        "📘 README"
    ])

    with tab_cap3_resumo:
        st.subheader("📌 Contexto da Atividade")

        st.write("""
        Em cooperativas agrícolas de pequeno porte, a classificação dos grãos pode ser
        feita manualmente por especialistas, o que torna o processo mais demorado e
        sujeito a erros humanos.

        Com Machine Learning, essa classificação pode ser automatizada, aumentando
        a eficiência e a precisão do processo.
        """)

        st.subheader("🎯 Objetivo")

        st.info("""
        Desenvolver um modelo de aprendizado de máquina para classificar variedades
        de trigo com base em características físicas dos grãos.
        """)

        st.subheader("🌱 Variedades analisadas")

        st.markdown("""
        - **Kama**
        - **Rosa**
        - **Canadian**
        """)

        st.subheader("📊 Atributos do Dataset")

        st.markdown("""
        | Atributo | Descrição |
        |---|---|
        | Área | Medida da área do grão |
        | Perímetro | Comprimento do contorno do grão |
        | Compacidade | Relação entre área e perímetro |
        | Comprimento do núcleo | Eixo principal do grão |
        | Largura do núcleo | Eixo secundário do grão |
        | Coeficiente de assimetria | Medida da assimetria do grão |
        | Comprimento do sulco do núcleo | Comprimento do sulco central |
        """)

        st.subheader("🧠 Etapas realizadas")

        st.markdown("""
        - Análise exploratória dos dados
        - Estatísticas descritivas
        - Histogramas, boxplots e gráficos de dispersão
        - Tratamento de valores ausentes
        - Normalização ou padronização das variáveis
        - Separação treino/teste
        - Treinamento de diferentes algoritmos de classificação
        - Comparação por acurácia, precisão, recall, F1-score e matriz de confusão
        - Otimização com busca de hiperparâmetros quando necessário
        """)

    with tab_cap3_notebook:
        st.subheader("📓 Notebook - Seeds Classification ML")

        if CAP3_NOTEBOOK.exists():
            st.success(f"Arquivo encontrado: {CAP3_NOTEBOOK.relative_to(BASE_DIR)}")

            st.write("""
            O notebook contém a análise exploratória, pré-processamento,
            treinamento, comparação e avaliação dos modelos de classificação.
            """)

            with open(CAP3_NOTEBOOK, "rb") as f:
                st.download_button(
                    label="📥 Baixar notebook",
                    data=f,
                    file_name=CAP3_NOTEBOOK.name,
                    mime="application/octet-stream"
                )

            st.info("""
            Para visualizar ou executar o notebook, abra o arquivo no Jupyter Notebook,
            Google Colab ou VS Code com suporte a notebooks.
            """)

        else:
            st.warning("Notebook do CAP3 não encontrado.")
            st.code(str(CAP3_NOTEBOOK))

    with tab_readme_cap3:
        mostrar_readme(README_CAP3, "📘 README do CAP3")
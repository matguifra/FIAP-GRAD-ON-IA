from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"

FASE6_DIR = ASSETS_DIR / "fase6"
CAP1_DIR = FASE6_DIR / "cap1"

# CAP1
README_FILE = CAP1_DIR / "README.md"
REQUIREMENTS_FILE = CAP1_DIR / "requirements.txt"
DATA_YAML = CAP1_DIR / "data" / "dataset" / "data.yaml"
DATA_LOCAL_YAML = CAP1_DIR / "data_local.yaml"

NOTEBOOK = CAP1_DIR / "src" / "notebook" / "RivandoBezerraCavalcantiNeto_rm568235_pbl_fase6.ipynb"
SCRIPTS_DIR = CAP1_DIR / "src" / "scripts"
RESULTS_DIR = CAP1_DIR / "docs" / "results"
EP30_DIR = RESULTS_DIR / "ep30"
EP60_DIR = RESULTS_DIR / "ep60"

# Ir Além
# Ir Além
IR_ALEM_DIR = CAP1_DIR / "ir_alem"
IR_ALEM_README = IR_ALEM_DIR / "README.md"
IR_ALEM_NOTEBOOK = IR_ALEM_DIR / "LeticiaAngelimGuerra_rm567501_pbl_fase6_ir_alem.ipynb"
IR_ALEM_ARQUITETURA = IR_ALEM_DIR / "assets" / "arquitetura.svg"

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

st.title("👁️ Fase 6 - Visão Computacional com YOLOv5")

st.write("""
Nesta fase, foi desenvolvido um projeto de visão computacional com YOLOv5,
demonstrando o treinamento e avaliação de um detector customizado para duas
classes: vacas e cachorros.
""")

st.divider()

tab_cap1, tab_ir_alem = st.tabs([
    "📌 CAP1 - YOLOv5",
    "🚀 Ir Além"
])


# =========================
# CAP1
# =========================
with tab_cap1:
    st.header("📌 CAP1 - Visão Computacional com YOLOv5")

    st.write("""
    O projeto organiza um dataset com 80 imagens, sendo 40 de vacas e 40 de
    cachorros. As imagens foram divididas em treino, validação e teste, com
    labels no formato YOLO. O modelo foi treinado em duas configurações:
    30 épocas e 60 épocas.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Imagens", "80")
    col2.metric("Classes", "2")
    col3.metric("Experimentos", "30 vs 60 épocas")

    st.divider()

    tab_resumo, tab_dataset, tab_notebook, tab_scripts, tab_resultados, tab_readme_cap1 = st.tabs([
        "📌 Resumo",
        "📂 Dataset",
        "📓 Notebook",
        "🧾 Scripts",
        "📊 Resultados",
        "📘 README"
    ])

    # =========================
    # RESUMO
    # =========================
    with tab_resumo:
        st.subheader("📌 Objetivo da Atividade")

        st.write("""
        O objetivo foi criar um sistema de visão computacional usando YOLO para
        demonstrar seu potencial em um cenário prático. O grupo escolheu duas
        classes bem distintas: **cow** e **dog**.
        """)

        st.subheader("🧠 Pipeline desenvolvido")

        st.markdown("""
        - Coleta automatizada de imagens
        - Divisão determinística em treino, validação e teste
        - Rotulação automática em formato YOLO
        - Treinamento com YOLOv5
        - Comparação entre 30 e 60 épocas
        - Avaliação com métricas como precision, recall e mAP
        - Geração de prints e inferências para comprovar os resultados
        """)

        st.subheader("🎥 Vídeo demonstrativo")

        st.video("https://youtu.be/nzV1QY16FQk")

        st.subheader("📊 Resultados principais")

        st.markdown("""
        | Experimento | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
        |---|---:|---:|---:|---:|
        | `cowdog_ep30` | 0.802 | 0.829 | 0.822 | 0.446 |
        | `cowdog_ep60` | 0.854 | 0.781 | 0.824 | 0.581 |
        """)

        st.info("""
        A versão com 60 épocas teve melhora relevante em mAP@0.5:0.95,
        indicando maior precisão nas bounding boxes, mesmo com leve queda no recall.
        """)

    # =========================
    # DATASET
    # =========================
    with tab_dataset:
        st.subheader("📂 Estrutura do Dataset")

        st.write("""
        O dataset foi organizado no padrão YOLO, com pastas separadas para treino,
        validação e teste, cada uma contendo imagens e labels.
        """)

        st.code("""
data/dataset/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
""", language="text")

        if DATA_YAML.exists():
            st.success(f"Arquivo encontrado: {DATA_YAML.relative_to(BASE_DIR)}")
            conteudo = DATA_YAML.read_text(encoding="utf-8", errors="ignore")
            st.code(conteudo, language="yaml")
        else:
            st.warning("Arquivo data.yaml não encontrado.")
            st.code(str(DATA_YAML))

        st.divider()

        for nome, pasta in {
            "Treino - imagens": CAP1_DIR / "data" / "dataset" / "train" / "images",
            "Treino - labels": CAP1_DIR / "data" / "dataset" / "train" / "labels",
            "Validação - imagens": CAP1_DIR / "data" / "dataset" / "val" / "images",
            "Validação - labels": CAP1_DIR / "data" / "dataset" / "val" / "labels",
            "Teste - imagens": CAP1_DIR / "data" / "dataset" / "test" / "images",
            "Teste - labels": CAP1_DIR / "data" / "dataset" / "test" / "labels",
        }.items():
            if pasta.exists():
                arquivos = [a for a in pasta.iterdir() if a.is_file()]
                st.write(f"✅ **{nome}:** {len(arquivos)} arquivo(s)")
            else:
                st.write(f"⚠️ **{nome}:** pasta não encontrada")

    # =========================
    # NOTEBOOK
    # =========================
    with tab_notebook:
        st.subheader("📓 Notebook End-to-End")

        if NOTEBOOK.exists():
            st.success(f"Arquivo encontrado: {NOTEBOOK.relative_to(BASE_DIR)}")

            st.write("""
            O notebook principal reúne o pipeline completo: preparação do dataset,
            treinamento, validação, inferência e comparação dos experimentos.
            """)

            with open(NOTEBOOK, "rb") as f:
                st.download_button(
                    label="📥 Baixar notebook da Fase 6",
                    data=f,
                    file_name=NOTEBOOK.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Notebook da Fase 6 não encontrado.")
            st.code(str(NOTEBOOK))

        st.info("""
        Para executar, abra o notebook no Google Colab, Jupyter Notebook ou VS Code
        com suporte a notebooks.
        """)

    # =========================
    # SCRIPTS
    # =========================
    with tab_scripts:
        st.subheader("🧾 Scripts Auxiliares")

        st.write("""
        Os scripts automatizam etapas como download de imagens, divisão do dataset,
        geração de labels YOLO e diagnóstico das anotações.
        """)

        if SCRIPTS_DIR.exists():
            scripts = sorted(SCRIPTS_DIR.glob("*.py"))

            if scripts:
                script_escolhido = st.selectbox(
                    "Selecione um script para visualizar",
                    scripts,
                    format_func=lambda x: x.name
                )

                codigo = script_escolhido.read_text(encoding="utf-8", errors="ignore")
                st.code(codigo, language="python")

                with open(script_escolhido, "rb") as f:
                    st.download_button(
                        label=f"📥 Baixar {script_escolhido.name}",
                        data=f,
                        file_name=script_escolhido.name,
                        mime="text/x-python"
                    )
            else:
                st.info("Nenhum script Python encontrado.")
        else:
            st.warning("Pasta de scripts não encontrada.")
            st.code(str(SCRIPTS_DIR))

    # =========================
    # RESULTADOS
    # =========================
    with tab_resultados:
        st.subheader("📊 Resultados e Evidências")

        st.write("""
        Esta seção mostra os resultados visuais dos experimentos com 30 e 60 épocas,
        incluindo inferências, curvas de treino e matriz de confusão.
        """)

        tab_ep30, tab_ep60 = st.tabs([
            "📉 30 épocas",
            "📈 60 épocas"
        ])

        def mostrar_galeria_resultados(pasta_resultados):
            if not pasta_resultados.exists():
                st.warning("Pasta de resultados não encontrada.")
                st.code(str(pasta_resultados))
                return

            imagens = sorted(
                list(pasta_resultados.rglob("*.png")) +
                list(pasta_resultados.rglob("*.jpg")) +
                list(pasta_resultados.rglob("*.jpeg"))
            )

            if not imagens:
                st.info("Nenhuma imagem encontrada nesta pasta.")
                return

            st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

            imagem_destaque = st.selectbox(
                "Selecione uma imagem para visualizar em destaque",
                imagens,
                format_func=lambda x: x.name,
                key=str(pasta_resultados)
            )

            st.image(
                str(imagem_destaque),
                caption=imagem_destaque.name,
                use_container_width=True
            )

            st.divider()

            colunas = st.columns(3)

            for index, imagem in enumerate(imagens):
                with colunas[index % 3]:
                    st.image(
                        str(imagem),
                        caption=imagem.name,
                        use_container_width=True
                    )

        with tab_ep30:
            mostrar_galeria_resultados(EP30_DIR)

        with tab_ep60:
            mostrar_galeria_resultados(EP60_DIR)


    # =========================
    # README CAP1
    # =========================
    with tab_readme_cap1:
        mostrar_readme(README_FILE, "📘 README do CAP1")


# =========================
# IR ALÉM
# =========================
with tab_ir_alem:
    st.header("🚀 Ir Além - Transfer Learning e Fine Tuning")

    st.write("""
    Esta seção apresenta o projeto **Ir Além** da Fase 6, usando Transfer Learning
    e Fine Tuning para comparar abordagens de classificação de imagens no dataset
    `cow` vs `dog`.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Modelo base", "MobileNetV2")
    col2.metric("Framework", "TensorFlow/Keras")
    col3.metric("Segmentação", "rembg / U²-Net")

    st.divider()

    tab_ir_resumo, tab_ir_arquitetura, tab_ir_notebook, tab_ir_readme = st.tabs([
        "📌 Resumo",
        "🏗️ Arquitetura",
        "📓 Notebook",
        "📘 README",
    ])

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
    # README IR ALÉM
    # =========================
    with tab_ir_readme:
        mostrar_readme(IR_ALEM_README, "📘 README do Ir Além")

    # =========================
    # RESUMO
    # =========================
    with tab_ir_resumo:
        st.subheader("📌 Objetivo")

        st.write("""
        O objetivo do Ir Além foi testar se uma rede pré-treinada na ImageNet
        consegue superar uma CNN treinada do zero em um dataset pequeno, além de
        avaliar se remover o fundo das imagens melhora a classificação.
        """)

        st.subheader("🧪 Hipóteses avaliadas")

        st.markdown("""
        - Redes pré-treinadas performam melhor do que redes treinadas do zero?
        - A remoção do fundo por segmentação melhora a classificação?
        """)

        st.subheader("🧠 Estratégia usada")

        st.markdown("""
        - Uso da **MobileNetV2** pré-treinada na ImageNet;
        - Congelamento inicial das camadas da rede base;
        - Treinamento de uma camada final para classificação binária;
        - Fine Tuning nas últimas 20 camadas;
        - Criação de um dataset paralelo com fundo removido usando `rembg`;
        - Comparação entre imagens originais e imagens segmentadas.
        """)

        st.subheader("📊 Resultados")

        st.markdown("""
        | Abordagem | Treino | Validação | Teste | Tempo |
        |---|---:|---:|---:|---:|
        | Transfer Learning - imagens originais | 100% | 87,5% | 100% | ~41s |
        | Transfer Learning + Fine Tuning | 100% | 100% | 100% | ~30s |
        | Transfer Learning - imagens sem fundo | 100% | 100% | 87,5% | ~40s |
        """)

        st.info("""
        O melhor resultado veio com Transfer Learning + Fine Tuning. A remoção
        de fundo não melhorou o desempenho, possivelmente porque o contexto visual
        das imagens ajudava a MobileNetV2 na classificação.
        """)

        st.subheader("🎥 Vídeo demonstrativo")

        st.video("https://youtu.be/0Ky0SZkz3NI")

    # =========================
    # ARQUITETURA
    # =========================
    with tab_ir_arquitetura:
        st.subheader("🏗️ Arquitetura do Projeto")

        st.write("""
        O fluxo compara dois caminhos: imagens originais e imagens com fundo
        removido. Ambos passam pela MobileNetV2, depois por treinamento inicial
        e Fine Tuning, gerando os resultados finais de classificação.
        """)

        if IR_ALEM_ARQUITETURA.exists():
            st.image(
                str(IR_ALEM_ARQUITETURA),
                caption="Arquitetura do projeto Ir Além",
                use_container_width=True
            )
        else:
            st.warning("Arquivo arquitetura.svg não encontrado.")
            st.code(str(IR_ALEM_ARQUITETURA))

    # =========================
    # NOTEBOOK
    # =========================
    with tab_ir_notebook:
        st.subheader("📓 Notebook - Ir Além")

        if IR_ALEM_NOTEBOOK.exists():
            st.success(f"Arquivo encontrado: {IR_ALEM_NOTEBOOK.relative_to(BASE_DIR)}")

            st.write("""
            O notebook contém a implementação com Transfer Learning, Fine Tuning,
            segmentação com `rembg` e comparação dos resultados.
            """)

            with open(IR_ALEM_NOTEBOOK, "rb") as f:
                st.download_button(
                    label="📥 Baixar notebook do Ir Além",
                    data=f,
                    file_name=IR_ALEM_NOTEBOOK.name,
                    mime="application/octet-stream"
                )

            st.info("""
            Para executar, abra o notebook no Google Colab, Jupyter Notebook ou
            VS Code com suporte a notebooks.
            """)
        else:
            st.warning("Notebook do Ir Além não encontrado.")
            st.code(str(IR_ALEM_NOTEBOOK))

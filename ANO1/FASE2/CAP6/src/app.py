import json, os, datetime
from typing import Dict, Any, List
from getpass import getpass
import oracledb

# =========================
# CAP. 3 — SUBALGORITMOS
# =========================
# O código inteiro é estruturado em subalgoritmos.


def input_int(
    prompt: str, min_val: int | None = None, max_val: int | None = None
) -> int:
    """Lê um inteiro do terminal, com validação opcional de faixa."""
    while True:  # loop até receber input válido
        try:
            # limpa espaços em branco antes e depois do input e tenta converter para int
            v = int(input(prompt).strip())
            if min_val is not None and v < min_val:  # checa se é menor que o mínimo
                print(f"Valor deve ser >= {min_val}.")
                continue
            if max_val is not None and v > max_val:  # checa se é maior que o máximo
                print(f"Valor deve ser <= {max_val}.")
                continue
            return v
        except ValueError:  # se a conversão para int falhar
            print("Digite um número inteiro válido.")


def input_float(
    prompt: str, min_val: float | None = None, max_val: float | None = None
) -> float:
    """Lê um float do terminal, com validação opcional de faixa."""
    while True:  # loop até receber input válido
        try:
            # limpa espaços em branco antes e depois do input, converte possível vírgula
            # em ponto e tenta converter para float
            v = float(input(prompt).replace(",", ".").strip())
            if min_val is not None and v < min_val:  # checa se é menor que o mínimo
                print(f"Valor deve ser >= {min_val}.")
                continue
            if max_val is not None and v > max_val:  # checa se é maior que o máximo
                print(f"Valor deve ser <= {max_val}.")
                continue
            return v
        except ValueError:  # se a conversão para float falhar
            print("Digite um número decimal válido (use . ou ,).")


def input_nonempty(prompt: str) -> str:
    """Lê uma string não vazia do terminal."""
    while True:  # loop até receber input válido
        # limpa espaços em branco antes e depois do input
        v = input(prompt).strip()
        if v:  # checa se não está vazio
            return v
        print("Campo obrigatório.")  # se vazio, avisa e repete


def limpar_console():
    """Limpa o console/terminal."""
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux e macOS
    else:
        os.system("clear")


# =========================
# CAP. 4 — ESTRUTURAS
# =========================
# Declara a estrutura de dados central do projeto, que é um dicionário de talhões e
# colheitas, que armazenará os dados durante a execução do programa e servirá como
# base para criar/carregar arquivo JSON e interagir com banco de dados da Oracle.
# "talhoes" é um dicionário de dicionários e "operacoes" é uma lista de dicionários.
# cada talhão e operação é um dicionário.
# Exemplo:
# {
#   "talhoes": {
#     "1": {"nome": "Talhão 1", "area_ha": 10.0},
#     "2": {"nome": "Talhão 2", "area_ha": 15.0}
#   },
#   "operacoes": [
#     {"id_talhao": 1, "data": "2023-01-01", "peso_t_colhido": 5.0, "perda_percent": 10.0},
#     {"id_talhao": 2, "data": "2023-01-02", "peso_t_colhido": 7.0, "perda_percent": 5.0}
#   ]
# }
db_mem = {"talhoes": {}, "operacoes": []}


def gerar_id_talhao(db: Dict[str, Any]) -> int:
    """Gera um novo ID para talhão, baseado nos existentes na memória."""
    if db["talhoes"]:  # se houver pelo menos um talhão
        # converte os IDs (chaves do dicionário) para inteiros e retorna um iterador
        iteravel_ids = map(int, db["talhoes"].keys())
        return max(iteravel_ids) + 1  # retorna o maior valor do iterador + 1
    else:
        return 1  # se não houver talhão, começa do 1


# =========================
# CAP. 5 — JSON + TXT
# =========================
CAMINHO_JSON = "dados.json"


def salvar_json(caminho: str, dados: Dict[str, Any]) -> None:
    """Salva os dados em um arquivo JSON formatado."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def carregar_json(caminho: str) -> Dict[str, Any]:
    """Carrega os dados de um arquivo JSON, se existir. Se não, retorna estrutura vazia."""
    if not os.path.exists(caminho):
        return {"talhoes": {}, "operacoes": []}
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def exportar_relatorio_txt(db: Dict[str, Any], caminho: str = "relatorio.txt") -> None:
    """Produz um relatório em um arquivo .txt com tabela alinhada."""
    # total de operações é o tamanho da lista de operações
    total_ops = len(db["operacoes"])  
    # cria uma lista com as perdas de cada operação, ou 0.0 se não houver operações
    perdas = [op["perda_percent"] for op in db["operacoes"]] or [0.0]
    media_perda = sum(perdas) / len(perdas)
    total_peso = (
        # se db["operacoes"] não estiver vazia, cria uma sequencia com os pesos colhidos
        # em cada operação e soma, senão retorna 0.0
        sum(op["peso_t_colhido"] for op in db["operacoes"])
        if db["operacoes"]
        else 0.0
    )

    # Prepara dados para tabela alinhada (se houver operações)
    talhao_map = db.get("talhoes", {})
    # cria uma lista onde será armazenada cada linha da tabela
    linhas = []
    for op in db["operacoes"]:
        # Obtém o nome do talhão a partir do id_talhao, ou "?" se não encontrar
        nome_t = talhao_map.get(str(op.get("id_talhao")), {}).get("nome", "?")
        # preenche a lista com dicionários representando cada linha
        linhas.append(
            {
                "data": str(op.get("data", "")),
                "id_talhao": str(op.get("id_talhao")),
                "nome": nome_t,
                "peso": float(op.get("peso_t_colhido", 0.0)),
                "perda": float(op.get("perda_percent", 0.0)),
            }
        )

    # escreve o relatório no arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("RELATÓRIO DE COLHEITA DE CANA\n")
        f.write("=" * 70 + "\n")
        f.write(
            f"Data de geração: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )
        f.write("RESUMO GERAL\n")
        f.write("-" * 70 + "\n")
        f.write(f"Total de operações: {total_ops}\n")
        f.write(f"Peso total colhido (t): {total_peso:.2f}\n")
        f.write(f"Média de perda estimada (%): {media_perda:.2f}\n\n")

        if linhas:
            # Calcula larguras das colunas aqui, quando já sabemos que a lista de linhas
            # não está vazia
            w_data = max(len("Data"), max(len(l["data"]) for l in linhas))
            w_id = max(len("ID"), max(len(l["id_talhao"]) for l in linhas))
            w_nome = max(len("Talhão"), max(len(l["nome"]) for l in linhas))
            w_peso = max(len("Peso(t)"), max(len(f"{l['peso']:.2f}") for l in linhas))
            w_perda = max(
                len("Perda(%)"), max(len(f"{l['perda']:.2f}") for l in linhas)
            )

            f.write("OPERAÇÕES DE COLHEITA\n")
            f.write("-" * 70 + "\n")

            # Cabeçalho da tabela
            header = f"{{:<{w_data}}} | {{:>{w_id}}} | {{:<{w_nome}}} | {{:>{w_peso}}} | {{:>{w_perda}}}"
            f.write(header.format("Data", "ID", "Talhão", "Peso(t)", "Perda(%)") + "\n")
            total_width = w_data + w_id + w_nome + w_peso + w_perda + 12
            f.write("-" * total_width + "\n")

            # Linhas de dados
            row_fmt = f"{{:<{w_data}}} | {{:>{w_id}}} | {{:<{w_nome}}} | {{:>{w_peso}.2f}} | {{:>{w_perda}.2f}}"
            for l in linhas:
                f.write(
                    row_fmt.format(
                        l["data"], l["id_talhao"], l["nome"], l["peso"], l["perda"]
                    )
                    + "\n"
                )
        else:
            f.write("Nenhuma operação registrada.\n")

        f.write("\n" + "=" * 70 + "\n")

    limpar_console()
    print(f"Relatório exportado em: {os.path.abspath(caminho)}")


# =========================
# CAP. 6 — ORACLE
# =========================
# Funções para ler credenciais e estabelecer conexão com Oracle


def oracle_enabled() -> bool:
    """
    Verifica se as variáveis de ambiente necessárias para conexão com a Oracle estão definidas.
    """
    # checa se ORA_DSN, ORA_USER e ORA_PASS estão definidas em os.environ
    # retorna True se todas existirem, senão False
    return all(k in os.environ for k in ["ORA_DSN", "ORA_USER", "ORA_PASS"])


def oracle_conn():
    """Cria e retorna uma conexão com o banco Oracle usando variáveis de ambiente."""
    return oracledb.connect(
        user=os.environ["ORA_USER"],
        password=os.environ["ORA_PASS"],
        dsn=os.environ["ORA_DSN"],
    )


def pedir_credenciais_oracle() -> bool:
    """
    Pede ORA_USER / ORA_PASS / ORA_DSN no terminal,
    testa a conexão e, se OK, guarda em os.environ (apenas nesta execução).
    """
    print("\n=== Configuração Oracle ===")
    print("Informe suas credenciais.")

    user = input_nonempty("Usuário: ")
    dsn = input_nonempty("DSN: ")
    passwd = getpass("Senha: ")

    # coloca nas variáveis de ambiente da sessão atual
    os.environ["ORA_USER"] = user
    os.environ["ORA_PASS"] = passwd
    os.environ["ORA_DSN"] = dsn

    # testa conexão
    try:
        with oracle_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT 'OK' FROM dual")
                _ = cur.fetchone()
        print("✅ Conexão Oracle validada com sucesso.")
        return True
    except Exception as e:
        print(f"❌ Não foi possível conectar no Oracle: {e}")
        # limpa se falhou
        for k in ("ORA_USER", "ORA_PASS", "ORA_DSN"):
            if k in os.environ:
                del os.environ[k]
        return False


def oracle_config_ok() -> bool:
    """
    Garante que credenciais existam e funcionem.
    Se não existirem, chama o assistente acima.
    """
    if oracle_enabled():
        try:
            with oracle_conn() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT 1 FROM dual")
                    _ = cur.fetchone()
            return True
        except Exception as e:
            print(f"⚠️ Variáveis ORA_* existem, mas a conexão falhou: {e}")
            print("Vamos tentar configurar novamente…")
            return pedir_credenciais_oracle()
    else:
        return pedir_credenciais_oracle()


# DDLs para criar as tabelas talhoes e operacoes

DDL_TALHOES = """
CREATE TABLE talhoes (
  id_talhao NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  nome VARCHAR2(100) NOT NULL,
  area_ha NUMBER(10,2) NOT NULL
)
"""

DDL_OPERACOES = """
CREATE TABLE operacoes (
  id_op NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  id_talhao NUMBER NOT NULL REFERENCES talhoes(id_talhao),
  data_op DATE NOT NULL,
  peso_t_colhido NUMBER(12,2) NOT NULL,
  perda_percent NUMBER(5,2) NOT NULL
)
"""

# =========================
# CAP. 6 — ORACLE
# =========================
# Funções para criar tabelas, listar talhões e operações (CRUD de leitura)


def oracle_criar_tabelas():
    """Cria as tabelas talhoes e operacoes, se não existirem."""
    try:
        # abre conexão e cria um cursor usando gerenciador de contexto
        with oracle_conn() as con, con.cursor() as cur:
            for ddl in (DDL_TALHOES, DDL_OPERACOES):
                try:
                    cur.execute(ddl)  # executa cada DDL
                    con.commit()  # confirma a transação
                # se falhar, informa o erro, mas ignora erro de tabela já existente
                except Exception as e:
                    if "ORA-00955" not in str(e):
                        print(f"[Oracle] Erro criando tabela: {e}")
        print("Tabelas conferidas/criadas.")
    # se a conexão falhar, mostra o erro
    except Exception as e:
        print(f"[Oracle] Erro criando tabelas: {e}")


def oracle_listar_talhoes() -> List[Dict[str, Any]]:
    """Retorna uma lista de talhões do banco Oracle."""
    try:
        with oracle_conn() as con, con.cursor() as cur:  # abre conexão e cria cursor
            # executa a comando SQL
            cur.execute(
                "SELECT id_talhao, nome, area_ha FROM talhoes ORDER BY id_talhao"
            )
            # produz uma lista de dicionários iterando sobre as linhas retornadas pelo
            # cursor
            return [
                {"id_talhao": row[0], "nome": row[1], "area_ha": float(row[2])}
                for row in cur
            ]
    # se a conexão ou consulta falhar, mostra o erro e retorna lista vazia
    except Exception as e:
        print(f"[Oracle] Erro listando talhões: {e}")
        return []


def oracle_listar_operacoes() -> List[Dict[str, Any]]:
    """Retorna uma lista de operações de colheita do banco Oracle."""
    try:
        with oracle_conn() as con, con.cursor() as cur:  # abre conexão e cria cursor
            # executa a comando SQL
            cur.execute(
                "SELECT id_op, id_talhao, TO_CHAR(data_op,'YYYY-MM-DD'), peso_t_colhido, perda_percent "
                "FROM operacoes ORDER BY id_op"
            )
            # produz uma lista de dicionários iterando sobre as linhas retornadas pelo
            # cursor
            return [
                {
                    "id_op": row[0],
                    "id_talhao": row[1],
                    "data": row[2],
                    "peso_t_colhido": float(row[3]),
                    "perda_percent": float(row[4]),
                }
                for row in cur
            ]
    # se a conexão ou consulta falhar, mostra o erro e retorna lista vazia
    except Exception as e:
        print(f"[Oracle] Erro listando operações: {e}")
        return []


# ================
# LÓGICA (Cap. 2)
# ================


def perda_alerta(perda_percent: float) -> str:
    """Gera um alerta textual baseado na perda percentual."""
    # Heurística simples: alerta por faixas
    if perda_percent >= 15:
        return "ALTA (investigar regulagem da colhedora, velocidade de avanço, altura de corte)"
    if perda_percent >= 8:
        return "MÉDIA (rever umidade e terreno, checar facas)"
    return "BAIXA (dentro do esperado)"


# =========================
# MENU/CRUD em memória
# =========================


def menu():
    """Mostra as opções do sistema."""
    print("\n=== GESTÃO DE COLHEITA DE CANA ===")
    print("1) Cadastrar talhão")
    print("2) Listar talhões")
    print("3) Registrar operação de colheita")
    print("4) Listar operações")
    print("5) Exportar relatório .txt")
    print("6) Salvar JSON")
    print("7) Carregar JSON")
    print("8) Oracle: sincronizar MEM -> Oracle")
    print("0) Sair")


def cadastrar_talhao():
    """Adiciona um talhão na memória."""
    # inputs com validação
    nome = input_nonempty("Nome do talhão: ")
    area = input_float("Área (ha): ", min_val=0.1)
    # gera novo ID e adiciona novo talhão no dicionário de talhões
    new_id = gerar_id_talhao(db_mem)
    db_mem["talhoes"][str(new_id)] = {
        "id_talhao": new_id,
        "nome": nome,
        "area_ha": area,
    }
    limpar_console()
    print(f"Talhão {new_id} criado.")


def listar_talhoes():
    """Mostra os talhões cadastrados na memória."""
    talhoes = db_mem["talhoes"]
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    # Calcula larguras das colunas
    valores = list(talhoes.values())
    largura_id = max(len("ID"), max(len(str(t["id_talhao"])) for t in valores))
    largura_nome = max(len("Nome"), max(len(str(t["nome"])) for t in valores))
    largura_area = max(
        len("Área (ha)"), max(len(f"{float(t['area_ha']):.2f}") for t in valores)
    )

    # Monta modelo de linhas (ID à direita, Nome à esquerda, Área à direita)
    header_fmt = f"{{:>{largura_id}}} | {{:<{largura_nome}}} | {{:>{largura_area}}}"
    row_fmt = f"{{:>{largura_id}}} | {{:<{largura_nome}}} | {{:>{largura_area}.2f}}"

    limpar_console()
    print(header_fmt.format("ID", "Nome", "Área (ha)"))  # cabeçalho
    print("-" * (largura_id + largura_nome + largura_area + 6))  # linha separadora
    # itera sobre os talhões e mostra cada um seguindo o modelo
    for t in valores:
        print(row_fmt.format(t["id_talhao"], t["nome"], t["area_ha"]))


def registrar_operacao():
    """Adiciona uma operação de colheita na memória."""
    if not db_mem["talhoes"]:  # se não houver talhões, avisa e cancela
        print("Cadastre talhões antes.")
        return
    listar_talhoes()  # mostra os talhões para o usuário escolher
    id_t = input_int("ID do talhão a ser colhido: ", min_val=1)  # qual talhão?
    if str(id_t) not in db_mem["talhoes"]:  # se o ID não existir, avisa e cancela
        print("Talhão inexistente.")
        return
    # inputs com validação
    data_str = input_nonempty("Data (YYYY-MM-DD): ")
    peso = input_float("Peso colhido (t): ", min_val=0.0)
    perda = input_float("Perda estimada (%): ", min_val=0.0, max_val=100.0)
    # cria o dicionário da operação de colheita
    op = {
        "id_op": len(db_mem["operacoes"]) + 1,
        "id_talhao": id_t,
        "data": data_str,
        "peso_t_colhido": peso,
        "perda_percent": perda,
        "alerta_perda": perda_alerta(perda),
    }
    # adiciona na lista de operações
    db_mem["operacoes"].append(op)
    limpar_console()
    print(f"Operação registrada. Alerta de perda: {op['alerta_perda']}")


def listar_operacoes():
    """Mostra as operações de colheita registradas na memória."""
    # se a lista de operações estiver vazia, avisa e cancela
    if not db_mem["operacoes"]:
        print("Nenhuma operação registrada.")
        return
    ops = db_mem["operacoes"]
    talhao_map = db_mem.get("talhoes", {})

    # Prepara valores calculados para cada coluna
    linhas = []
    for op in ops:
        nome_t = talhao_map.get(str(op.get("id_talhao")), {}).get("nome", "?")
        talhao_txt = f"{op.get('id_talhao')} ({nome_t})"
        linhas.append(
            {
                "id": str(op.get("id_op")),
                "data": str(op.get("data", "")),
                "talhao": talhao_txt,
                "peso": float(op.get("peso_t_colhido", 0.0)),
                "perda": float(op.get("perda_percent", 0.0)),
                "alerta": str(op.get("alerta_perda", "")),
            }
        )

    # Larguras dinâmicas
    w_id = max(len("ID"), max(len(l["id"]) for l in linhas))
    w_data = max(len("Data"), max(len(l["data"]) for l in linhas))
    w_talhao = max(len("Talhão"), max(len(l["talhao"]) for l in linhas))
    w_peso = max(len("Peso(t)"), max(len(f"{l['peso']:.2f}") for l in linhas))
    w_perda = max(len("Perda(%)"), max(len(f"{l['perda']:.2f}") for l in linhas))
    w_alerta = max(len("Alerta"), max(len(l["alerta"]) for l in linhas))

    header_fmt = f"{{:>{w_id}}} | {{:<{w_data}}} | {{:<{w_talhao}}} | {{:>{w_peso}}} | {{:>{w_perda}}} | {{:<{w_alerta}}}"
    row_fmt = f"{{:>{w_id}}} | {{:<{w_data}}} | {{:<{w_talhao}}} | {{:>{w_peso}.2f}} | {{:>{w_perda}.2f}} | {{:<{w_alerta}}}"

    limpar_console()
    print(header_fmt.format("ID", "Data", "Talhão", "Peso(t)", "Perda(%)", "Alerta"))
    total_width = w_id + w_data + w_talhao + w_peso + w_perda + w_alerta + 3 * (6 - 1)
    print("-" * total_width)
    for l in linhas:
        print(
            row_fmt.format(
                l["id"], l["data"], l["talhao"], l["peso"], l["perda"], l["alerta"]
            )
        )


def sincronizar_mem_para_oracle():
    """
    Sincroniza os dados da memória para o banco Oracle.
    """
    # se as credenciais não foram declaradas como variáveis de ambiente, avisa e pede
    if not oracle_enabled():
        print("Defina ORA_DSN / ORA_USER / ORA_PASS nas variáveis de ambiente.")
        pedir_credenciais_oracle()
        return

    # se as credenciais estão registradas, cria as tabelas
    oracle_criar_tabelas()

    # 1) Sincroniza TALHÕES preservando o id_talhao da memória
    print("\nSincronizando talhões...")
    # cria um conjunto com os IDs dos talhões já existentes no Oracle
    existentes_oracle = {t["id_talhao"] for t in oracle_listar_talhoes()}
    # cria uma lista com os talhões que estão na memória, mas não no Oracle, iteraando
    # sobre os talhões na memória e filtrando pelos que não estão no conjunto acima
    novos_talhoes = [
        t for t in db_mem["talhoes"].values() if t["id_talhao"] not in existentes_oracle
    ]
    # se a lista acima não estiver vazia
    if novos_talhoes:
        with oracle_conn() as con, con.cursor() as cur:  # abre conexão e cria cursor
            # itera sobre os talhões novos
            for t in novos_talhoes:
                try:
                    # insere os novos talhões com comando SQL
                    cur.execute(
                        "INSERT INTO talhoes (id_talhao, nome, area_ha) VALUES (:1, :2, :3)",
                        [t["id_talhao"], t["nome"], t["area_ha"]],
                    )
                    print(
                        f"✅ Talhão '{t['nome']}' (ID {t['id_talhao']}) inserido no Oracle."
                    )
                # se a inserção falhar, mostra o erro
                except Exception as e:
                    print(
                        f"❌ Falha ao inserir talhão '{t['nome']}' (ID {t['id_talhao']}): {e}"
                    )
            # confirma a transação
            con.commit()
        # Atualiza o conjunto de existentes para a etapa das operações
        existentes_oracle |= {t["id_talhao"] for t in novos_talhoes}
    else:  # se não houver talhões novos, avisa
        print("Nenhum novo talhão para sincronizar.")

    print("\nSincronizando operações...")
    # cria uma lista com as operações já existentes no banco Oracle
    ops_oracle = oracle_listar_operacoes()
    # itera sobre as operações da lista acima criada e cria um conjunto de tuplas
    # (id_talhao, data, peso_t_colhido, perda_percent)
    # cada tupla representa uma operação de colheita única
    conjunto_op_oracle = {
        (
            op["id_talhao"],
            op["data"],
            float(op["peso_t_colhido"]),
            float(op["perda_percent"]),
        )
        for op in ops_oracle
    }

    # cria uma lista com as operações que estão na memória, mas não no Oracle e cujo
    # talhão existe no Oracle
    novas_operacoes = []
    for op in db_mem["operacoes"]:  # itera sobre as operações de colheita na memória
        # se o talhão da colheita não existir no Oracle, avisa e ignora
        if op["id_talhao"] not in existentes_oracle:
            print(
                f"⚠️ Operação {op['id_op']} ignorada. Talhão {op['id_talhao']} não existe no Oracle."
            )
            continue
        # cria uma tupla que representa uma operação de colheita
        op_na_memoria = (
            op["id_talhao"],
            op["data"],
            float(op["peso_t_colhido"]),
            float(op["perda_percent"]),
        )
        # se a tupla acima não existir no conjunto de operações do Oracle, adiciona na
        # lista de novas operações
        if op_na_memoria not in conjunto_op_oracle:
            novas_operacoes.append(op)

    # se houver novas operações
    if novas_operacoes:
        with oracle_conn() as con, con.cursor() as cur:  # abre conexão e cria cursor
            # itera sobre as novas operações
            for op in novas_operacoes:
                try:
                    # insere a operação com comando SQL
                    cur.execute(
                        "INSERT INTO operacoes (id_talhao, data_op, peso_t_colhido, perda_percent) "
                        "VALUES (:1, TO_DATE(:2,'YYYY-MM-DD'), :3, :4)",
                        [
                            op["id_talhao"],
                            op["data"],
                            op["peso_t_colhido"],
                            op["perda_percent"],
                        ],
                    )
                    print(
                        f"✅ Operação {op['id_op']} (talhão {op['id_talhao']}) inserida."
                    )
                # se a inserção falhar, mostra o erro
                except Exception as e:
                    print(f"❌ Falha ao inserir operação {op['id_op']}: {e}")
            # confirma a transação
            con.commit()
    else:
        print("Nenhuma nova operação para sincronizar.")

    print("\nSincronização concluída.")


def main():
    """
    Executa um loop interativo que apresenta um menu de opções para o usuário
    realizar operações relacionadas ao cadastro e gerenciamento de talhões e
    operações agrícolas.
    """

    while True:
        menu()  # mostra as opções
        opcao = input_nonempty("Escolha: ")

        if opcao == "1":
            cadastrar_talhao()
        elif opcao == "2":
            listar_talhoes()
        elif opcao == "3":
            registrar_operacao()
        elif opcao == "4":
            listar_operacoes()
        elif opcao == "5":
            exportar_relatorio_txt(db_mem)
        elif opcao == "6":
            salvar_json(CAMINHO_JSON, db_mem)
            limpar_console()
            print(f"Salvo em {CAMINHO_JSON}.")
        elif opcao == "7":
            db = carregar_json(CAMINHO_JSON)  # carrega o JSON do arquivo na variável
            # se o JSON for um dicionário e tiver as chaves "talhoes" e "operacoes"
            if isinstance(db, dict) and "talhoes" in db and "operacoes" in db:
                # insere os dados carregados do arquivo JSON no dicionário em memória
                db_mem.update(db)
                limpar_console()
                print("JSON carregado na memória.")
            else:
                limpar_console()
                print("JSON inválido.")
        elif opcao == "8":
            print("\n=== Sincronizar MEM -> Oracle ===")
            if oracle_config_ok():  # se a conexão com o Oracle estiver OK
                # sobe os dados do dicionário em memória para o banco Oracle
                sincronizar_mem_para_oracle()
        elif opcao == "0":
            limpar_console()
            print("Até mais!")
            break
        else:
            limpar_console()
            print("Opção inválida.")


if __name__ == "__main__":
    main()

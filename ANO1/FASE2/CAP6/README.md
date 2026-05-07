# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Cap 6 - Python e além

## Grupo 15

## 👨‍🎓 Integrantes: 
- João Rafael Gonçalves Ramos
- Letícia Angelim Guerra
- Matheus Guimarães França
- Rivando Bezerra Cavalcanti Neto
- Tales Ferraz de Arruda Domienikan

## 👩‍🏫 Professores:
### Tutor(a) 
- Ana Cristina dos Santos
### Coordenador(a)
- André Godoi Chiovato


## 📜 Descrição

O agronegócio representa a totalidade das atividades econômicas interligadas à produção e comercialização de produtos agrícolas. Longe de se restringir apenas ao cultivo em fazendas, ele constitui uma vasta e complexa cadeia produtiva que funciona como a base da supply chain de inúmeros outros segmentos, impactando diretamente o cotidiano das pessoas. Sendo um dos setores que mais gera empregos no mundo, especialmente no Brasil, sua importância é fundamental não apenas para a economia, mas também para o desenvolvimento social e a segurança alimentar global.

O conceito moderno de agronegócio trata os diferentes elos de sua cadeia como um sistema integrado e interdependente. Este sistema começa com os agricultores, que utilizam técnicas cada vez mais sofisticadas — incluindo geolocalização e agricultura de precisão — para cultivar lavouras e criar animais. Em paralelo, a agroindústria desenvolve maquinário avançado, como colheitadeiras autônomas com piloto automático, para aumentar a eficiência no campo. Subsequentemente, as indústrias de processamento transformam a matéria-prima em produtos intermediários ou finais, otimizando processos de embalagem e transporte. Embora cada etapa não interaja diretamente com o consumidor final, a eficiência coletiva de toda a cadeia é crucial para manter os preços competitivos e garantir o abastecimento do mercado.

O principal objetivo do agronegócio é levar um produto agrícola, de forma eficiente, do campo até o consumidor. Para isso, ele é estruturado em cinco setores produtivos principais:

- **Setor de Insumos:** Engloba o fornecimento de todos os produtos e serviços necessários para a produção, como sementes, fertilizantes, defensivos agrícolas e maquinário.

- **Setor de Produção:** Corresponde à atividade primária, ou seja, o cultivo de culturas e a criação de gado.

- **Setor de Processamento e Transformação:** Composto por indústrias que recebem a matéria-prima e a transformam em produtos, como laticínios, frigoríficos e usinas de açúcar.

- **Setor de Distribuição e Consumo:** Encarregado de fazer os produtos chegarem ao consumidor final por meio de canais de logística, marketing e varejo.

- **Setor de Serviços de Apoio:** Inclui todos os serviços essenciais para o funcionamento da cadeia, como financiamento, seguros, consultoria técnica e pesquisa.

Um dos pilares do agronegócio contemporâneo é a inovação. O setor é um dos que mais investe em tecnologia para aprimorar seus processos, desde a inteligência artificial aplicada ao monitoramento de lavouras até sistemas de gestão que automatizam operações. Nesse contexto, surgem as agrotechs: startups focadas em desenvolver soluções tecnológicas para o campo. Diferente das consultorias tradicionais, que oferecem conhecimento técnico, as agrotechs criam ferramentas (softwares, aplicativos, sensores) que empoderam o produtor. Esses recursos facilitam a coleta e a análise de dados, permitindo uma visão ampliada do negócio e auxiliando na tomada de decisões estratégicas para otimizar a produtividade e a gestão da propriedade de forma contínua.

Apesar de seu sucesso e avanço tecnológico, o setor enfrenta desafios significativos. Um exemplo prático é o da cana-de-açúcar no Brasil. Embora o país seja líder mundial na produção, as perdas durante a colheita mecanizada podem chegar a 15%, um percentual que representa um prejuízo anual de milhões de reais para os produtores e para a economia. Isso demonstra a necessidade constante de otimização por meio de melhor planejamento, escolha do momento ideal para a colheita e uso mais eficiente das máquinas. 

**Esta solução é um sistema de gestão de operações de colheita de cana-de-açúcar que alerta o agricultor caso a taxa de perda esteja muito alta (mais que 15%), média (mais que 8%) ou baixa (menor que 8%). Ele é capaz de armazenar os dados inseridos em um relatório em arquivo txt, arquivo json ou em um banco de dados da Oracle.**


## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*

Antes de tudo, é necessário instalar o oracledb em seu ambiente de execução fazendo `pip install oracledb` em seu terminal.

Somente o arquivo app.py é necessário, então simplesmente execute-o, seja em uma IDE ou no terminal com o comando "python app.py".

## Sobre o código

Ao executar o código, a função main() é chamada. A função main() inicia um loop que chama a função menu() para exibir as opções disponíveis para o usuário. Cada opção que o usuário escolher chama sua respectiva função.

Antes de explicar as opções, é importante entender a estrutura do banco de dados (db) utilizado no código. O db é um dicionário que contém duas chaves principais: "talhoes" e "operacoes". A chave "talhoes" armazena informações sobre os talhões cadastrados como dicionários, enquanto a chave "operacoes" armazena informações sobre as operações de colheita realizadas como uma lista de dicionários, ou seja, cada talhão e operação de colheita são dicionários.

Além disso, todas as entradas de dados são validadas por funções específicas para garantir que os dados inseridos estejam corretos. Cada função de input garante que o usuário insira um valor válido, seja um número inteiro, um número decimal ou ou string, todos não vazios e dentro dos limites estabelecidos.

Há também função de limpeza de tela, que verifica qual o sistema operacional do usuário e executa o comando adequado para limpar a tela.

### Opções do menu:
#### Opção 1 - Cadastrar Talhão: cadastrar_talhao()
Solicita ao usuário que insira o ID, nome e área do talhão.<br>
Após validar as entradas, é chamada a função gerar_id_talhao() para gerar um id, que é o próximo número inteiro do maior id já cadastrado.<br>
O talhão é então adicionado ao dicionário "talhoes" no banco de dados (db), e a tela é limpa com uma mensagem de sucesso.
##### gerar_id_talhao()
Transforma as chaves do dicionário "talhoes" em uma lista de inteiros, encontra o maior valor e retorna o próximo número inteiro como o novo id.
#### Opção 2 - Listar Talhões: listar_talhoes()
Verifica se há talhões cadastrados.<br>
Se não houver, exibe uma mensagem informando que não há talhões cadastrados e cancela a operação.<br>
Caso contrário, calcula a largura máxima de cada coluna (ID, Nome, Área) para formatar a saída, cria um modelo de cabeçalho e linhas, limpa a tela e exibe a tabela formatada com os talhões cadastrados.
#### Opção 3 - Registrar Operação: registrar_operacao()
Registra colheita.<br>
Verifica se há talhões cadastrados. Se não houver, exibe uma mensagem informando que é necessário cadastrar um talhão antes de registrar uma operação e cancela a operação.<br>
Caso contrário, lista os talhões cadastrados e solicita ao usuário que insira o ID do talhão a ser colhido; se não existir, exibe uma mensagem de erro e cancela a operação.<br>
Escolhido o talhão, solicita a data da operação, a quantidade colhida (em toneladas) e a quantidade perdida (em porcentagem).<br>
Após validar as entradas, é preparado um dicionário com os dados da operação, incluindo o alerta de perda, que é determinado pela função calcular_alerta_perda().<br>
A operação é então adicionada à lista "operacoes" no banco de dados (db), e a tela é limpa e uma mensagem de sucesso é exibida.
##### perda_alerta(perda_percent: float) -> str
Retorna um alerta de perda com base na porcentagem de perda informada. Menor que 8% é "Baixa", entre 8% e 15% é "Média" e maior que 15% é "Alta".
#### Opção 4 - Listar Operações: listar_operacoes()
Verifica se há operações registradas.<br>
Se não houver, exibe uma mensagem informando que não há operações registradas e cancela a operação.<br>
Caso contrário, obtém todos os talhões e colheitas cadastradas e prepara uma lista de linhas para preencher a tabela com os todos os dados.<br>
Calcula a largura máxima de cada coluna (ID, Data, Talhão, Peso(t), Perda(%), Alerta) para formatar a saída, cria um modelo de cabeçalho e linhas, limpa a tela e exibe a tabela formatada com as operações registradas.
#### Opção 5 - Gerar Relatório: exportar_relatorio()
Primeiro, são calculadas algumas métricas, como o total de operações, a soma do peso colhido e a média de perda.<br>
Depois, os dados são preparados para a tabela alinhada, semelhante à função listar_operacoes(), onde é criada uma lista de dicionários representando cada linha da tabela a partir de todos os talhões e operações no banco de dados (db).<br>
Com a lista de linhas pronta, é aberto um arquivo de texto chamado "relatorio.txt" em modo de escrita.<br>
É escrito o cabeçalho do relatório, seguido pelas métricas calculadas.<br>
Se houver operações, são calculadas as larguras máximas de cada coluna (ID, Data, Talhão, Peso(t), Perda(%), Alerta) para formatar a saída da tabela e criados os modelos de cabeçalho e linhas.<br>
Então, a tabela é escrita no arquivo, seguida por um aviso de onde está o arquivo salvo.<br>
#### Opção 6 - Salvar JSON: salvar_json()
É chamada a função salvar_json() passando o caminho e os dados do banco de dados (db), o console é limpo e uma mensagem de sucesso é exibida.
##### salvar_json(caminho: str, dados: Dict[str, Any]) -> None
Abre um arquivo JSON no caminho especificado em modo de escrita e grava os dados do banco de dados (db) no arquivo com indentação para melhor legibilidade.
#### Opção 7 - Carregar JSON: carregar_json()
É chamada a função carregar_json() passando o caminho, daí verifica se os dados retornados são um dicionário e se contêm as chaves "talhoes" e "operacoes".<br>
Se sim, o banco de dados (db) é atualizado com os dados carregados, o console é limpo e uma mensagem de sucesso é exibida.<br>
Se não, o console é limpo e uma mensagem de erro é exibida.
##### carregar_json(caminho: str) -> Dict[str, Any]
Verifica se o arquivo JSON no caminho especificado existe. Se não existir, retorna um dicionário vazio.<br>
Se existir, abre o arquivo em modo de leitura e carrega os dados do JSON, retornando-os como um dicionário.
#### Opção 8 - Oracle: sincronizar MEM -> Oracle: sincronizar_mem_para_oracle()
Primeiro, é chamada a função oracle_config_ok() para verificar se a configuração do Oracle está correta.<br>
Se estiver, é chamada a função sincronizar_mem_para_oracle() para sincronizar os dados do banco de dados em memória (db_mem) para o banco de dados Oracle.<br>
##### oracle_config_ok() -> bool
Chama oracle_enabled() para verificar se as credenciais de acesso ao Oracle foram declaradas nas variáveis de ambiente.<br>
Se foram, tenta estabelecer uma conexão com o banco de dados Oracle chamando oracle_conn(), criando um cursor, executando uma consulta de teste e descartando o resultado.<br>
Se a conexão for bem-sucedida, retorna True. Se houver qualquer erro, exibe uma mensagem de erro e chama a função pedir_credenciais_oracle() para solicitar as credenciais ao usuário.<br>
##### oracle_enabled() -> bool
Verifica se as variáveis de ambiente necessárias para a conexão com o Oracle (ORA_USER, ORA_PASS, ORA_DSN) estão definidas e não estão vazias. Retorna True se todas estiverem definidas, caso contrário, retorna False.
##### oracle_conn()
Tenta estabelecer uma conexão com o banco de dados Oracle usando as credenciais fornecidas nas variáveis de ambiente (ORA_USER, ORA_PASS, ORA_DSN) e retorna o objeto de conexão.
##### pedir_credenciais_oracle() -> bool
Solicita ao usuário que insira as credenciais de acesso ao Oracle (usuário, senha e DSN) e define essas credenciais como variáveis de ambiente (ORA_USER, ORA_PASS, ORA_DSN).<br>
Tenta estabelecer uma conexão com o Oracle chamando oracle_conn() e tentando executar uma consulta de teste.<br>
Se bem sucedido, exibe uma mensagem de sucesso e retorna True. Se houver qualquer erro, exibe uma mensagem de erro, limpa as variáveis de ambiente e retorna False.
##### sincronizar_mem_para_oracle()
Verifica se as credenciais do Oracle foran declaradas como variáveis de ambiente, se não, exibe alerta e pede as credenciais chamando pedir_credenciais_oracle().<br>
Se as credenciais estiverem corretas, chama oracle_criar_tabelas() para criar as tabelas necessárias no Oracle.<br>
Em seguida, obtém todos os talhões que estão no banco de dados da Oracle chamando oracle_listar_talhoes() e armazena os IDs em um conjunto para evitar duplicatas.<br>
Depois, identifica os talhões que estão no banco de dados em memória (db_mem) mas não estão no Oracle, e os insere em uma lista.<br>
Se houver talhões para inserir, abre conexão com o Oracle, cria um cursor itera sobre os talhões a serem inseridos, executando uma instrução INSERT para cada um e exibindo na tela.<br>
Após inserir todos os talhões, confirma as alterações com commit().<br>
Atualiza o conjunto de IDs de talhões no Oracle e repete o processo para as operações, identificando as que estão no banco de dados em memória (db_mem) mas não estão no Oracle, chamando oracle_listar_operacoes(), inserindo-as em um conjunto.<br>
Cria uma lista de operações a serem inseridas iterando sobre as operações no banco de dados em memória (db_mem) e verificando se o ID da operação não está no conjunto de IDs de operações no Oracle. Se não estiver, adiciona a operação à lista de operações a serem inseridas.<br>
Se houver operações para inserir, abre conexão com o Oracle, cria um cursor e itera sobre as operações a serem inseridas, executando uma instrução INSERT para cada uma e exibindo na tela.<br>
Após inserir todas as operações, confirma as alterações com commit() e informa sucesso.<br>
##### oracle_criar_tabelas()
Abre conexão com o Oracle, cria um cursor e executa instruções SQL para criar as tabelas "talhoes" e "operacoes" se elas não existirem.<br>
As instruções SQL estão pré-definidas como strings chamadas DDL_TALHOES e DDL_OPERACOES.<br>
Informa sucesso ou falha na criação das tabelas.
##### oracle_listar_talhoes() -> List[Dict[str, Any]]
Abre conexão com o Oracle, cria um cursor e executa uma consulta SQL para selecionar todos os talhões da tabela "talhoes".<br>
Obtém os resultados da consulta e os retorna em uma lista de dicionários, onde cada dicionário representa um talhão.<br>
Em caso de erro, exibe uma mensagem de erro e retorna uma lista vazia.
##### oracle_listar_operacoes() -> List[Dict[str, Any]]
Abre conexão com o Oracle, cria um cursor e executa uma consulta SQL para selecionar todas as operações da tabela "operacoes".<br>
Obtém os resultados da consulta e os retorna em uma lista de dicionários, onde cada dicionário representa uma operação.<br>
Em caso de erro, exibe uma mensagem de erro e retorna uma lista vazia.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

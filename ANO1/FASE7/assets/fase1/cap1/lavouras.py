def calculo(tipo_lavoura):
    #Estabelecendo coeficientes e constantes
    if tipo_lavoura == 1:
        tipo = "soja"
        produtividade = 3900  # kg
        extracao_nitrogenio = 0  # g
        extracao_fosforo = 0.0154  # g
        extracao_potassio = 0.038  # g
        extracao_agua = 0.025  # mm
    else:
        tipo = "milho"
        produtividade = 12000  # kg
        extracao_nitrogenio = 0.022  # g
        extracao_fosforo = 0.009  # g
        extracao_potassio = 0.022  # g
        extracao_agua = 0.02  # mm

    # Cálculo da área de plantio
    print("Insira as dimensões da lavoura")
    while True:
        try:
            largura = float(input("Largura em metros: "))
            comprimento = float(input("Comprimento em metros: "))
            break
        except:
            print("Digite um valor valido!\n")
            continue

    hectares = largura * comprimento / 10000
    print(f"\nSua nova lavoura de {tipo} tem {hectares:,.3f} hectares.")

    # Calculo da quantidade de adubo e água que a plantação extrai do solo (EMBRAPA 2013)
    nitrogenio = hectares * produtividade * extracao_nitrogenio
    fosforo = hectares * produtividade * extracao_fosforo
    potassio = hectares * produtividade * extracao_potassio
    irrigacao = largura * comprimento * extracao_agua
    agua = largura * comprimento * 0.8
    print(
        f"Considerando um solo corrigido típico do Cerrado, com produtividade alvo de {produtividade}kg/ha (média Mato Grosso) e limpo, a plantação consumirá:\n"
        f"Nitrogenio (N): {nitrogenio:.3f}kg\n"
        f"Fósforo (P₂O₅): {fosforo:,.3f}kg\n"
        f"Potássio (K₂O): {potassio:,.3f}kg\n"
        f"Água total    : {agua:,.3f}m³\n"
        f"Quando o solo atingir 50% de umidade, deve-se irrigar com {irrigacao:,.3f}m³ de água.\n")

    return tipo, hectares, nitrogenio, fosforo, potassio, agua, irrigacao

lavouras = []

while True:
    print("\nBem vindo ao Sistema de Gestão de sua lavoura!\n"
          "[1] Consultar lavouras\n"
          "[2] Inserir nova lavoura\n"
          "[3] Atualizar lavoura\n"
          "[4] Remover lavoura\n"
          "[5] Produzir string com todos os dados\n"
          "[6] Sair\n")

    #Tentativa de capturar opção
    try:
        opcao = int(input("Opção: "))
        # Avalia se a opção é correta
        if opcao not in [1, 2, 3, 4, 5, 6]:
            print("\nOpção invalida!\n\n")
            continue
    except:
        print("\nOpção inválida!\n")
        continue

    #Sair do programa
    if opcao == 6:
        break

    #Consultar lavoura
    if opcao == 1:
        if not lavouras: #Verifica se há alguma lavoura
            print("\nNão há lavouras!\n")
            continue
        else:
            for lavoura in lavouras:
                print(f"\nLavoura {lavoura['id']}:\n"
                      f"Tipo      : {lavoura['tipo']}\n"
                      f"Area      : {lavoura['area']:,.3f} hectares\n"
                      f"Nitrogênio: {lavoura['nitrogenio']:,.3f}kg\n"
                      f"Fósforo   : {lavoura['fosforo']}kg\n"
                      f"Potássio  : {lavoura['potassio']:,.3f}kg\n"
                      f"Água      : {lavoura['agua']:,.3f}m³\n"
                      f"Irrigação : {lavoura['irrigacao']:,.3f}")

    #Inserção de nova lavoura
    if opcao == 2:
        while True:
            print("Escolha o tipo de cultura:\n"
                  "[1] Soja\n"
                  "[2] Milho\n"
                  "[3] Cancelar\n")

            #Tentativa de capturar opção
            try:
                opcao_lavoura = int(input("Cultura: "))
                # Avalia se a opção é correta
                if opcao_lavoura not in [1, 2, 3]:
                    print("\nOpção invalida!\n")
                    continue
            except:
                print("\nOpção inválida!\n")
                continue

            #Cancela a inserção
            if opcao_lavoura == 3:
                break

            #Checa se a lista de lavouras está vazia e define um ID
            if not lavouras:
                ID = 1
            else:
                ID = lavouras[-1]['id'] + 1

            print(f"\nCriando lavoura {ID}.")

            # Calculo de todos atributos da lavoura
            tipo, hectares, nitrogenio, fosforo, potassio, agua, irrigacao = calculo(opcao_lavoura)

            #Inserção da lavoura no vetor
            lavouras.append({"id" : ID,
                             "tipo" : tipo,
                             "area" : hectares,
                             "nitrogenio" : nitrogenio,
                             "fosforo" : fosforo,
                             "potassio" : potassio,
                             "agua" : agua,
                             "irrigacao" : irrigacao})
            break

    #Atualização de lavoura
    if opcao == 3:
        #Verifica se há alguma lavoura
        if not lavouras:
            print("\nNão há lavouras!\n")
            continue
        while True:
            print("Qual lavoura será atualizada?")

            #Tentativa de capturar id
            try:
                ID = int(input("ID: "))
                # Checagem se lavoura existe
                existe = False
                for lavoura in lavouras:
                    if lavoura["id"] == ID:
                        existe = True
                if not existe:
                    print("\nLavoura não existe!\n")
                    break
            except:
                print("\nOpção inválida!\n")
                continue

            print("\nEscolha o novo tipo de cultura:\n"
                  "[1] Soja\n"
                  "[2] Milho\n"
                  "[3] Cancelar\n")

            #Tentativa de capturar tipo de lavoura
            try:
                opcao_lavoura = int(input("Cultura: "))
                # Avalia se a opção é correta
                if opcao_lavoura not in [1, 2, 3]:
                    print("\nOpção invalida!\n")
                    continue
            except:
                print("\nOpção inválida!\n")
                continue

            # Cancela a inserção
            if opcao_lavoura == 3:
                break

            # Calculo de todos atributos da lavoura
            tipo, hectares, nitrogenio, fosforo, potassio, agua, irrigacao = calculo(opcao_lavoura)

            # Atualização da lavoura no vetor
            for i, lavoura in enumerate(lavouras):
                if lavoura['id'] == ID:
                    lavouras[i]['tipo'] = tipo
                    lavouras[i]['area'] = hectares
                    lavouras[i]['nitrogenio'] = nitrogenio
                    lavouras[i]['fosforo'] = fosforo
                    lavouras[i]['potassio'] = potassio
                    lavouras[i]['agua'] = agua
                    lavouras[i]['irrigacao'] = irrigacao
                    break
            break

    #Remoção de lavoura
    if opcao == 4:
        #Verifica se existe alguma lavoura
        if not lavouras:
            print("\nNão há lavouras!\n")
            continue
        print("Insira o ID da lavoura a ser removida.")
        #Tentativa de capturar ID
        try:
            ID = int(input("ID: ")) #Identificação da lavoura a ser removida
        except:
            print("\nOpção inválida!\n")
            continue
        #Busca pela lavoura no vetor
        for i, lavoura in enumerate(lavouras):
            if lavoura['id'] == ID:
                del lavouras[i] #Remoção
                break

    if opcao == 5:
        #Produzir lista dos dados para facilitar levar os dados para o script R
        if not lavouras:
            print("\nNão há lavouras!\n")
            continue
        else:
            lista_dados = []
            for lavoura in lavouras:
                lista_dados.append(lavoura['area'])
                lista_dados.append(lavoura['nitrogenio'])
                lista_dados.append(lavoura['fosforo'])
                lista_dados.append(lavoura['potassio'])
                lista_dados.append(lavoura['agua'])
                lista_dados.append(lavoura['irrigacao'])
            #Printa os dados separados por virgula para copiar e colar no vetor do script R
            print(lista_dados)
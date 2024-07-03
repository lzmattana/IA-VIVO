import textwrap

def menu():
    menu = """\n
    ############################
    #### BEM VINDO AO BANCO ####
    ### ESCOLHA UMA OPERAÇÃO ###

    [d]\tDEPOSITAR VALOR
    [s]\tSACAR VALOR
    [e]\tCONSULTAR EXTRATO
    [cu]\tCRIAR USUÁRIO
    [ac]\tABRIR CONTA
    [lc]\tLISTAR CONTAS
    [x]\tENCERRAR A OPERAÇÃO

    ############################
    ############################
    >>  """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"DEPÓSITO:\tR$ {valor:.2f}\n"
        print("\n## DEPÓSITO REALIZADO COM SUCESSO ##")
    else:
        print("\n## VALOR INFORMADO É INVÁLIDO ##")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n## Falha na operação! O valor informado é inválido. ##")
        return saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n## Falha na operação! Você não tem saldo suficiente. ##")
    elif excedeu_limite:
        print("\n## Falha na operação! O valor do saque excede o limite de saque único. ##")
    elif excedeu_saques:
        print("\n## Falha na operação! Número máximo de saque diário excedido. ##")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n!!! Saque realizado! Recolha seu dinheiro. !!!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n############# EXTRATO #############\n")
    print("NÃO FORAM REALIZADAS TRANSAÇÕES." if not extrato else extrato)
    print(f"\## SALDO:\t\tR$ {saldo:.2f}")
    print("\n###################################\n")

def criar_usuario(usuarios):
    cpf = input("DIGITE SEU CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n## JA EXISTE USUÁRIO COM ESSE CPF! ##")
        return

    nome = input("NOME COMPLETO: ")
    data_nascimento = input("DATA DE NASCIMENTO (dd-mm-aaaa): ")
    endereco = input("ENDEREÇO (Logradouro, nº - Bairro - Cidade/UF): ")

    usuarios.append({"NOME": nome, "DATA_NASCIMENTO": data_nascimento, "CPF": cpf, "ENDEREÇO": endereco})

    print("\n### USUÁRIO CRIADO COM SUCESSO! ###")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["CPF"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("INFORME SEU CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### CONTA CRIADA COM SUCESSO ###")
        return {"AGENCIA": agencia, "NUMERO_CONTA": numero_conta, "USUARIO": usuario}

    print("\n## USUÁRIO NÃO ENCONTRADO ##")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            AGÊNCIA:\t{conta['AGENCIA']}
            C/C:\t\t{conta['NUMERO_CONTA']}
            TITULAR:\t{conta['USUARIO']['NOME']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("INFORME VALOR A DEPOSITAR: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("INFORME O VALOR A SACAR: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "ac":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "x":
            break

        else:
            print("OPERAÇÃO INVÁLIDA")

main()
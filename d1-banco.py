menu = """

#### BEM-VINDO A SUA CONTA ####

[d] -> DEPOSITAR
[s] -> SACAR
[e] -> EXTRATO
[q] -> SAIR

###############################

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("# INFORME O VALOR DO DEPÓOSITO # -> "))

        if valor > 0:
            saldo += valor
            extrato += f"# DEPÓSITO # R$ {valor:.2f}\n"

        else:
            print("# VALOR INFORMADO ERRADO! #")

    if opcao == "s":
        valor = float(input("# INFORME O VALOR DO SAQUE # -> "))
        if valor > saldo:
            print("# SALDO INSUFICIENTE! #")
        elif valor > limite:
            print("# SAQUE EXCEDE O LIMITE! #")
        elif numero_saques >= LIMITE_SAQUES:
            print("# EXCEDEU O LIMETE DE SAQUES DIARIOS! #")
        elif valor > 0:
            saldo -= valor
            extrato += f"# SAQUE # R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("# VALOR INFORMADO INVALIDO! #")
   
    elif opcao == "e":
        print("\n### EXTRATO ###")
        print("# SEM MOVIMENTAÇÃO #" if not extrato else extrato)
        print(f"\n# SALDO # R$ {saldo:.2f}")
        print("##############")

    elif opcao == "q":
        break

    else:
        print("# OPERAÇÃO INVÁLIDA! #")
saldo = 0
historico_transacoes = []
lista_usuarios = []
LIMITE_SAQUE_DIARIO = 3
NUMERO_AGENCIA = "001"

def MENU():

    print("""
    --------------- MENU ---------------
        
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] CRIAR USUÁRIO
    [5] CRIAR CONTA
    [6] CANCELAR
        
    """)


def depositar(saldo, historico_transacoes, /):
    print("\n\n------------- DEPÓSITO -------------")

    valor_deposito = float(input("\nDigite o valor do depósito: R$"))


    if valor_deposito < 0:

        print("\n! ERRO: Valor de depósito inválido.")

    else:

        saldo += valor_deposito

        print(f"\n> Depósito de R${valor_deposito:.2f} realizado com sucesso!")

        historico_transacoes.append(f" Depósito: + R${valor_deposito:.2f}")

    return saldo, historico_transacoes


def sacar(*, LIMITE_SAQUE_DIARIO, saldo, historico_transacoes):
    
    if LIMITE_SAQUE_DIARIO != 0:

        print("\n\n------------- SAQUE -------------")

        valor_saque = float(input("\nDigite o valor do saque: R$"))


        if valor_saque <= 0:
                
            print("\n! ERRO: Valor de saque inválido.")

        elif valor_saque > 500:

            print ("\n! ERRO: O valor de saque máximo é de R$500,00")

                    
        elif saldo < valor_saque:

            print("ERRO: Saldo insuficiente.")


        else:

            saldo -= valor_saque
            LIMITE_SAQUE_DIARIO -= 1

            print(f"\n> Saque de R${valor_saque:.2f} realizado com sucesso!")

            historico_transacoes.append(f" Saque: - R${valor_saque:.2f}")


    else:

        print("\nERRO: Limite de saques diários atingidos.")

    
    return LIMITE_SAQUE_DIARIO, saldo, historico_transacoes



def exibir_historico_transacoes(saldo, /, *, historico_transacoes):

    if historico_transacoes == []:

        print("\n\n------------- EXTRATO -------------")
        print("\n > Não houve movimentações na conta.")
    

    else:

        print("\n\n------------- EXTRATO -------------")

        for transacao in historico_transacoes:
            print(transacao)

        print("-------------------------------------\n")
        print(f"> Saldo atual: R${saldo:.2f}")

    return


def criar_usuario(lista_usuarios):

    print("\n\n------------- CRIAR USUÁRIO -------------")
    
    cpf = input("\nDigite o seu CPF (somente números): ")

    for usuario in lista_usuarios:

        if usuario["cpf"] == cpf:

            print("\n ! ERRO: Já existe um usuário com o CPF digitado.")

            return
    
    nome = input("\nDigite o nome completo: ")
    data_nascimento = input("\nDigite a data de nascimento no formato (dd/mm/AAAA): ")
    cpf = cpf
    endereco = input("\nInforme o endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n > Usuário registrado com sucesso!")

    
def criar_conta(lista_usuarios, NUMERO_AGENCIA):

    print("\n\n------------- CRIAR CONTA -------------")

    cpf = input("\nDigite o seu CPF (somente números): ")

    for usuario in lista_usuarios:

        if usuario["cpf"] == cpf:

            numero_conta = 1


            if "contas" in usuario:

                numero_conta = len(usuario["contas"]) + 1

                nova_conta = {"agencia": NUMERO_AGENCIA, "numero_conta": numero_conta, "user": cpf}

                usuario["contas"].append(nova_conta)



            else:
                
                usuario["contas"] = [{"agencia": NUMERO_AGENCIA, "numero_conta": numero_conta, "user": cpf}]

            
            print("\nConta criada com sucesso! Aqui vão os dados das suas contas: \n")

            exibir_contas(usuario["contas"])

            return


    print("\n ! Usuário não registrado. Digite um usuário válido para criar uma nova conta.")
    return

def exibir_contas(contas):
    
    for conta in contas:
        print(f"====> CONTA {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"CPF do Titular: {conta['user']}")
        print("-------------------------------------------\n")


while True:

    MENU()

    seleciona_operacao = input("Digite o número da operação desejada: ")

    seleciona_operacao = int(seleciona_operacao)
        

    if seleciona_operacao == 1:

        saldo, historico_transacoes = depositar(saldo, historico_transacoes)


    if seleciona_operacao == 2:

        LIMITE_SAQUE_DIARIO, saldo, historico_transacoes = sacar(LIMITE_SAQUE_DIARIO=LIMITE_SAQUE_DIARIO, saldo=saldo, historico_transacoes=historico_transacoes)
        

    if seleciona_operacao == 3:

        exibir_historico_transacoes(saldo, historico_transacoes=historico_transacoes)

    if seleciona_operacao == 4:

        criar_usuario(lista_usuarios=lista_usuarios)

    if seleciona_operacao == 5:

        criar_conta(lista_usuarios=lista_usuarios, NUMERO_AGENCIA=NUMERO_AGENCIA)

    if seleciona_operacao == 6:

        break

    else:

        print("\n! Selecione uma opção válida")


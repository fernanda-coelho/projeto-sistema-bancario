
MENU = """
--------------- MENU ---------------
    
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[4] CANCELAR
    
"""


saldo = 0
historico_transacoes = ""
LIMITE_SAQUE_DIARIO = 3


while True:

    seleciona_operacao = input(MENU + "Digite o número da operação desejada: ")

    seleciona_operacao = int(seleciona_operacao)
    

    if seleciona_operacao == 1:

        print("\n\n------------- DEPÓSITO -------------")

        valor_deposito = float(input("\nDigite o valor do depósito: R$"))


        if valor_deposito < 0:

            print("\n! ERRO: Valor de depósito inválido.")

        else:

            saldo += valor_deposito

            print(f"\n> Depósito de R${valor_deposito:.2f} realizado com sucesso!")

            historico_transacoes += (f" Depósito: + R${valor_deposito:.2f} \n")


    if seleciona_operacao == 2:

        if LIMITE_SAQUE_DIARIO != 0:

            print("\n\n------------- SAQUE -------------")

            valor_saque = float(input("\nDigite o valor do saque: R$"))


            if valor_saque <= 0:
             
             print("\n! ERRO: Valor de saque inválido.")
        

            elif valor_saque > 500:

                print ("\n! ERRO: O valor de saque máximo é de R$500,00")

            else:
                
                if saldo >= valor_saque:

                    saldo -= valor_saque
                    LIMITE_SAQUE_DIARIO -= 1

                    print(f"\n> Saque de R${valor_saque:.2f} realizado com sucesso!")

                    historico_transacoes += (f" Saque: - R${valor_saque:.2f}\n")

                else:
                
                    print("ERRO: Saldo insuficiente.")

        else:

            print("\nERRO: Limite de saques diários atingidos.")
    

    if seleciona_operacao == 3:

        if historico_transacoes == "":

            print("Não houve movimentações na conta.")

        else:

            print("\n\n------------- EXTRATO -------------")
            print(historico_transacoes)
            print("-------------------------------------\n")
            print(f"> Saldo atual: R${saldo:.2f}")


    else: 
        break
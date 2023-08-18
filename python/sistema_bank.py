saldo = 0
depositos = []
saques = []

while True:
    print("\nEscolha a opção desejada:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            valor_deposito = input("Digite o valor do depósito: ")
            if valor_deposito.isdigit():
                valor_deposito = float(valor_deposito)
                if valor_deposito > 0:
                    saldo += valor_deposito
                    depositos.append(valor_deposito)
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido para depósito.")
            else:
                print("Valor inválido. Insira um número válido.")
        elif opcao == 2:
            valor_saque = input("Digite o valor do saque: ")
            if valor_saque.isdigit():
                valor_saque = float(valor_saque)
                if len(saques) < 3 and valor_saque <= 500 and valor_saque <= saldo:
                    saldo -= valor_saque
                    saques.append(valor_saque)
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                elif len(saques) >= 3:
                    print("Limite de saques diários atingido.")
                elif valor_saque > 500:
                    print("Valor máximo de saque é R$ 500.00.")
                else:
                    print("Saldo insuficiente ou valor inválido para saque.")
            else:
                print("Valor inválido. Insira um número válido.")
        elif opcao == 3:
            print(f"\nExtrato bancário:")
            if len(depositos) == 0 and len(saques) == 0:
                print("Não foram realizadas movimentações.")
            else:
                for deposito in depositos:
                    print(f"Depósito: R$ {deposito:.2f}")
                for saque in saques:
                    print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {saldo:.2f}")
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")
    else:
        print("Opção inválida. Insira um número válido.")

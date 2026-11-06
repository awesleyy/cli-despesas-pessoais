from . import transacoes


def exibir_menu():
    print("\n--- Sistema de Finanças ---")
    print("1 - Adicionar Transação.")
    print("2 - Listar Transações.")
    print("3 - Remover Transação.")
    print("4 - Total de Despesas.")
    print("5 - Saldo.")
    print("6 - Filtrar por Categoria.")
    print("0 - Sair")


def main():
    lista_transacoes = []

    while True:
        exibir_menu()
        try:
            opcao = int(input("\nDigite o número da opção que deseja: "))
        except ValueError:
            print("Dígito inválido.")
            continue
        if opcao == 0:
            break
        elif opcao == 1:
            pass #função 1
        elif opcao == 2:
            pass #função 2
        elif opcao == 3:
            pass #função 3
        elif opcao == 4:
            pass #função 4
        elif opcao == 5:
            pass #função 5
        elif opcao == 6:
            pass #função 6
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

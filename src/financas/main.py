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


def opcao_adicionar(lista_transacoes):
    pass


def opcao_listar(lista_transacoes):
    transacoes.listar_transacoes(lista_transacoes)


def opcao_remover(lista_transacoes):
    pass


def opcao_total_despesas(lista_transacoes):
    pass


def opcao_saldo(lista_transacoes):
    pass


def opcao_filtrar(lista_transacoes):
    pass


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
            opcao_adicionar(lista_transacoes)
        elif opcao == 2:
            opcao_listar(lista_transacoes)
        elif opcao == 3:
            opcao_remover(lista_transacoes)
        elif opcao == 4:
            opcao_total_despesas(lista_transacoes)
        elif opcao == 5:
            opcao_saldo(lista_transacoes)
        elif opcao == 6:
            opcao_filtrar(lista_transacoes)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

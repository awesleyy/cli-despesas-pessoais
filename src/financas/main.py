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
    try:
        posicao = int(input("Informe o número de transação: "))
    except ValueError:
        print("Digite um número inteiro.")
        return

    try:
        transacoes.remover_transacao(lista_transacoes, posicao)
    except ValueError as erro:
        print(erro)


def opcao_total_despesas(lista_transacoes):
    print(f"Valor Total das Despesas: R$ {transacoes.calcular_total_despesas(lista_transacoes):.2f}")


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

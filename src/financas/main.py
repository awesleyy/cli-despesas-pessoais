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
    while True:
        exibir_menu()
        try:
            opcao = int(input("\nDigite o número da opção que deseja: "))
        except ValueError:
            print("Dígito inválido.")
            continue
        if opcao == 0:
            break
        if opcao < 0 or opcao > 6:
            print("Digite um número de 0 a 6.")


if __name__ == "__main__":
    main()

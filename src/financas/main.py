from . import transacoes


def main():
    while True:
        print("\n--- Sistema de Finanças ---")
        print("1 - Adicionar Transação.")
        print("2 - Listar Transações.")
        print("3 - Remover Transação.")
        print("4 - Total de Despesas.")
        print("5 - Saldo.")
        print("6 - Filtrar por Categoria.")
        print("0 - Sair")
        opcao = int(input("\nDigite o número da opção que deseja:"))
        if opcao == 0:
            break
    

if __name__ == "__main__":
    main()

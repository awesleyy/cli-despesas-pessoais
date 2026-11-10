from .carteira import Carteira
from .transacao import Transacao


def exibir_menu():
    print("\n--- Sistema de Finanças ---")
    print("1 - Adicionar Transação.")
    print("2 - Listar Transações.")
    print("3 - Remover Transação.")
    print("4 - Total de Despesas.")
    print("5 - Saldo.")
    print("6 - Filtrar por Categoria.")
    print("0 - Sair")


def opcao_adicionar(carteira):
    try:
        valor = float(input("Informe o valor da transação: "))
    except ValueError:
        print("Digite somente números.")
        return

    categoria = input("Informe a categoria da transação: ")
    data = input("Informe a data da transação (Ano-Mês-Dia): ")
    tipo = input("Informe o tipo de transação ('receita' ou 'despesa'): ")

    try:
        nova_transacao = Transacao(valor, categoria, data, tipo)
        carteira.adicionar_transacao(nova_transacao)
        print("Transação adicionada com sucesso!")
    except ValueError as erro:
        print(erro)


def opcao_listar(carteira):
    carteira.listar_transacoes()


def opcao_remover(carteira):
    try:
        posicao = int(input("Informe o número de transação: "))
    except ValueError:
        print("Digite um número inteiro.")
        return

    try:
        carteira.remover_transacao(posicao)
        print("Transação removida com sucesso!")
    except ValueError as erro:
        print(erro)


def opcao_total_despesas(carteira):
    print(f"Valor Total das Despesas: R$ {carteira.calcular_total_despesas():.2f}")


def opcao_saldo(carteira):
    saldo = carteira.calcular_saldo()
    if saldo < 0:
        saldo = abs(saldo)
        print(f"Saldo Atual: -R$ {saldo:.2f}")
    else:
        print(f"Saldo Atual: R$ {saldo:.2f}")


def opcao_filtrar(carteira):
    categoria = input("Informe a categoria das transações que deseja filtrar: ")
    carteira_filtrada = carteira.filtrar_categoria(categoria)
    carteira_filtrada.listar_transacoes()


def main():
    carteira = Carteira()

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
            opcao_adicionar(carteira)
        elif opcao == 2:
            opcao_listar(carteira)
        elif opcao == 3:
            opcao_remover(carteira)
        elif opcao == 4:
            opcao_total_despesas(carteira)
        elif opcao == 5:
            opcao_saldo(carteira)
        elif opcao == 6:
            opcao_filtrar(carteira)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

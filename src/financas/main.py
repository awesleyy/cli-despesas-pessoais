from . import transacoes


def main():
    lista_despesas = []
    despesas = transacoes.calcular_total_despesas(lista_despesas)
    print(despesas)


if __name__ == "__main__":
    main()

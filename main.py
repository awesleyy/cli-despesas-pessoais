def adicionar_transacao(lista_transacoes, valor, categoria, data, tipo):

    nova_transacao = {
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "tipo": tipo
    }

    lista_transacoes.append(nova_transacao)


def listar_transacoes(lista_transacoes):
    if len(lista_transacoes) == 0:
        print("Lista de transações vazia.")
        return
        
    for posicao, transacao in enumerate(lista_transacoes):
        print(f"{posicao}: {transacao['data']}, {transacao['tipo']}, "
              f"{transacao['categoria']}, {transacao['valor']:.2f}")
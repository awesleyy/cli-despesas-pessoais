def adicionar_transacao(lista_transacoes, data, tipo, categoria, valor):

    nova_transacao = {
        "data": data,
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria
    }

    lista_transacoes.append(nova_transacao)


def listar_transacoes(lista_transacoes):
    if len(lista_transacoes) == 0:
        print("Lista de transações vazia.")
        return
        
    for posicao, transacao in enumerate(lista_transacoes):
        print(f"{posicao}: {transacao['data']}, {transacao['tipo']}, "
              f"{transacao['categoria']}, {transacao['valor']:.2f}")


def remover_transacao(lista_transacoes, posicao_transacao):
    return(lista_transacoes.pop(posicao_transacao))


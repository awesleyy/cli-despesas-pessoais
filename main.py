def adicionar_transacao(lista_transacoes, valor, categoria, data, tipo):

    nova_transacao = {
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "tipo": tipo
    }

    lista_transacoes.append(nova_transacao)

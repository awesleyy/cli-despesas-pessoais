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


def calcular_total_despesas(lista_transacoes):
    valor_despesas = 0
    for transacao in lista_transacoes:
        if transacao["tipo"] == "despesa":
            valor_despesas += transacao["valor"]
    return valor_despesas


def filtrar_categoria(lista_transacoes, categoria):
    lista_filtrada = []
    for transacao in lista_transacoes:
        if transacao["categoria"] == categoria:
            lista_filtrada.append(transacao)
    return lista_filtrada


def calcular_saldo(lista_transacoes):
    valor_receitas = 0
    for transacao in lista_transacoes:
        if transacao["tipo"] == "receita":
            valor_receitas += transacao["valor"]
    valor_despesas = calcular_total_despesas(lista_transacoes)

    return valor_receitas - valor_despesas

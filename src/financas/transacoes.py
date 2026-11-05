from datetime import datetime

def adicionar_transacao(lista_transacoes, valor, categoria, data, tipo):
    if not (isinstance(valor, (float, int))) or valor <= 0:
        raise ValueError("O valor não pode ser negativo ou igual a 0, e deve ser um número")
    try:
        datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Digite uma data válida.")
    if tipo != "despesa" and tipo != "receita":
        raise ValueError("Tipo da transação inválida, informe um tipo válido.")
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
    if not isinstance(posicao_transacao, int) or posicao_transacao >= len(lista_transacoes) or posicao_transacao < 0:
        raise ValueError("Posição inválida, informe uma posição válida")
    return lista_transacoes.pop(posicao_transacao)


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

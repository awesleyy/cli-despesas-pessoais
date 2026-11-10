from .transacao import Transacao


class Carteira:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, nova_transacao):
        if not isinstance(nova_transacao, Transacao):
            raise TypeError("Esperando um objeto Transacao")
        self._transacoes.append(nova_transacao)

    def listar_transacoes(self):
        if len(self._transacoes) == 0:
            print("Lista de transações vazia.")
            return

        for posicao, transacao in enumerate(self._transacoes):
            print(f"{posicao}: {transacao}")

    def remover_transacao(self, posicao_transacao):
        if not isinstance(posicao_transacao, int) or posicao_transacao >= len(self._transacoes) or posicao_transacao < 0:
            raise ValueError("Posição inválida, informe uma posição válida")
        return self._transacoes.pop(posicao_transacao)

    def calcular_total_despesas(self):
        valor_despesas = 0
        for transacao in self._transacoes:
            if transacao.tipo == "despesa":
                valor_despesas += transacao.valor
        return valor_despesas

    def calcular_saldo(self):
        valor_receitas = 0
        for transacao in self._transacoes:
            if transacao.tipo == "receita":
                valor_receitas += transacao.valor
        valor_despesas = self.calcular_total_despesas()
        return valor_receitas - valor_despesas

    def filtrar_categoria(self, categoria):
        carteira_filtrada = Carteira()
        for transacao in self._transacoes:
            if transacao.categoria == categoria:
                carteira_filtrada.adicionar_transacao(transacao)
        return carteira_filtrada

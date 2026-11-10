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

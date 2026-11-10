from .transacao import Transacao


class Carteira:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, nova_transacao):
        if not isinstance(nova_transacao, Transacao):
            raise TypeError("Esperando um objeto Transacao")
        self._transacoes.append(nova_transacao)

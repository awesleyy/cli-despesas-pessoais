import sqlite3
from .transacao import Transacao


class RepositorioTransacoes:
    def __init__(self, caminho_banco):
        self._conexao = sqlite3.connect(caminho_banco)
        cursor = self._conexao.cursor()
        comando_sql = """
        CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL NOT NULL CHECK (valor > 0),
        categoria TEXT NOT NULL,
        data TEXT NOT NULL,
        tipo TEXT NOT NULL
        )
        """
        cursor.execute(comando_sql)
        self._conexao.commit()

    def salvar_transacao(self, transacao):
        if not isinstance(transacao, Transacao):
            raise TypeError("Esperando um objeto Transacao")
        if transacao.id is not None:
            raise ValueError("Transação já salva.")
        cursor = self._conexao.cursor()
        cursor.execute("INSERT INTO transacoes (valor, categoria, data, tipo) VALUES (?, ?, ?, ?)",
                        (transacao.valor, transacao.categoria, transacao.data, transacao.tipo))
        self._conexao.commit()
        transacao.id = cursor.lastrowid

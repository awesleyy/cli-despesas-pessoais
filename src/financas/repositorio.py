import sqlite3


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
from datetime import datetime
import math


class Transacao:
    def __init__(self, valor, categoria, data, tipo):
        if not isinstance(valor, (float, int)) or valor <= 0 or not math.isfinite(valor):
            raise ValueError("O valor não pode ser negativo ou igual a 0, e deve ser um número")
        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Digite uma data válida.")
        if tipo != "despesa" and tipo != "receita":
            raise ValueError("Tipo da transação inválida, informe um tipo válido.")
        if not categoria.strip():
            raise ValueError("A categoria está vazia ou só contém espaços.")

        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.tipo = tipo

    def __str__(self):
        return f"{self.data}, {self.tipo}, {self.categoria}, {self.valor:.2f}"

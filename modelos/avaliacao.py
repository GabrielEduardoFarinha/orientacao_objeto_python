class Avaliacao:
    def __init__(self, cliente, nota):
        if not 1 <= nota <= 5:
            raise ValueError("A nota deve estar entre 1 e 5.")
        self._cliente = cliente
        self._nota = nota
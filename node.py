class Node:
    valor = 0
    proximo = Noneant = None

    def __init__(self, valor = 0, proximo = 0, ant = None):
        self.valor = valor
        self.proximo = proximo
        self.ant = ant
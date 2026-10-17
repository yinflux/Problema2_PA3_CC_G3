class Node:
    def __init__(self, data, horario, linha):
        self.data = data
        self.horario = horario
        self.linha = linha

        self.chave = (data, horario, linha)

        self.esquerdo = None
        self.direita = None

class ArvoreB:
    def __init__(self):
        self.raiz = None

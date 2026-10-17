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
        
    def registrar_chegada(self, data, horario, linha):
        regc = Node(data,horario,linha)

        if self.raiz == None:
            self.raiz = regc
            return
        atual = self.raiz
        while True:
            if regc < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = regc
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = regc
                    return
                atual = atual.direita

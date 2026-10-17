#Criando a classe principal da arvore de dados:
class Node:
    def __init__(self, data, horario, linha):
        self.data = data
        self.horario = horario
        self.linha = linha
        #Criando uma tupla(data, horario, linha), que em python ja faz a comparação lexicográfica
        self.chave = (data, horario, linha)

        self.esquerdo = None
        self.direita = None
#Craindo a classe ArvoreB que irá receber os principais comandos de inserir, remover, buscar
class ArvoreB:
    def __init__(self):
        self.raiz = None
        
    def registrar_chegada(self, data, horario, linha):
        #Inserindo uma nova chegada, regc recebe os dados necessários
        regc = Node(data,horario,linha)
        #Caso não tenha nenhum dado na raiz, regc passa a ser raiz
        if self.raiz == None:
            self.raiz = regc
            return "OK"
        #Copia a raiz como atual, temporariamente
        atual = self.raiz
        
        while True:
            #Se a chave(tupla) de regc for igual a chave atual, retorna "DUPLICADO"
            if regc.chave == atual.chave:
                return "DUPLICADO"
            #Recursivamente confere se regc é menor que a chave atual, se sim, se esquerda de atual estiver livre, regc entra nela, se esquerda n estiver vazia, atual é igual ao mesmo dado olhado na conferência anterior, o que isso faz com que recursivamente se "crie" uma subarvore a esquerda, até que a esquerda de atual esteja livre. 
            if regc < atual.chave:
                if atual.esquerda is None:
                    atual.esquerda = regc
                    return "OK"
                atual = atual.esquerda
            else:
            #Mesma lógica da esquerda, porém nesse caso agora para direita, ou seja, para valores maior que a chave atual
                if atual.direita is None:
                    atual.direita = regc
                    return "OK"
                atual = atual.direita
                

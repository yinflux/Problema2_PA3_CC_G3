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
    #R1: registrar_chegada(data, horario, linha)    
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
    #R6: remover_chegada(data, horario, linha)            
    def remover_chegada(self, data, horario, linha):
        chave_alvo = (data,horario,linha)
        pai = None
        atual = self.raiz

        while atual and atual.chave != chave_alvo:
            pai = atual
            if chave_alvo < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        if not atual: #Mesma coisa que dizer que if atual is None:
            return "NAO" 

        #Caso 1: 2 filhos -> substituir pelo min da direita
        if atual.esquerda and atual.direita:
            pai_suc = atual
            suc = atual.direita
            while suc.esquerda:
                pai_suc = suc
                suc = suc.esquerda
            #Copia a chave e os dados do sucessor
            atual.chave = suc.chave
            atual.data = suc.data
            atual.horario = suc.horario
            atual.linha = suc.linha
            # O nó a ser removido fisicamente vira o sucessor
            pai = pai_suc
            atual = suc

        #Caso 2: 0 ou 1 filho
        filho = atual.esquerda or atual.direita
        if pai is None:
            self.raiz = filho
        elif pai.esquerda == atual:
            pai.esquerda = filho
        else:
            pai.direita = filho
        return "OK"
                

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
            if regc.chave < atual.chave:
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
        
         # R2: BUSCAR CHEGADA(DATA, HORARIO, LINHA), INFORMA SE A CHEGADA ESTÁ REGISTRADA
    def buscar_chegada(self,data,horario,linha):
        atual = self.raiz

        while atual:
            if (data,horario,linha) == atual.chave:
                return "ACHOU"
            elif (data,horario,linha) < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return "NAO"


# Formatar a entrada de dados para garantir a consistência do formato antes de registrar, buscar ou remover chegadas
def formatar_entrada(data, horario, linha):
  #Remove espaços antes/depois e limita a 8 caracteres
  linha_formatada = linha.strip()[:8]

  #Aceita separadores como '/' ou '.' e converte para AAAA-MM-DD
  data_limpa = data.strip().replace('/', '-').replace('.', '-')
  partes_data = data_limpa.split('-')

  if len(partes_data) == 3:
    #Se o usuário digitou no formato(DD-MM-AAAA)
    if len(partes_data[0]) == 2 and len(partes_data[2]) == 4:
      dia, mes, ano = partes_data
      data_formatada = f'{ano}-{mes.zfill(2)}-{dia.zfill(2)}'
    #Se já digitou no formato(AAAA-MM-DD)
    else:
      ano, mes, dia = partes_data
      data_formatada = f'{ano}-{mes.zfill(2)}-{dia.zfill(2)}'
  else:
    data_formatada = data_limpa

  #Garante o horário no formato HH:MM:SS
  horario_limpo = horario.strip()
  partes_horario = horario_limpo.split(':')

  if len(partes_horario) == 2:
    hh, mm = partes_horario
    horario_formatado = f'{hh.zfill(2)}:{mm.zfill(2)}:00'
  elif len(partes_horario) == 3:
    hh, mm, ss = partes_horario
    horario_formatado = f'{hh.zfill(2)}:{mm.zfill(2)}:{ss.zfill(2)}'
  else:
    horario_formatado = horario_limpo

  return data_formatada, horario_formatado, linha_formatada


if __name__ == "__main__":

        opc = 0
        arv = ArvoreB()

        while opc != 4:
            print("1 - Registrar chegada")
            print("2 - Buscar chegada")
            print("3 - Remover chegada")
            print("4 - Sair")
            opc = int(input("Escolha uma opção: "))

            if opc == 1:
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")
                linhaf = input("Digite a linha: ")

                data, horario, linha = formatar_entrada(dataf, horariof, linhaf)

                resultado = arv.registrar_chegada(data, horario, linha)
                print(f"Entrada feita: {data}, {horario}, {linha}")
                print(resultado)

            elif opc == 2:
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")
                linhaf = input("Digite a linha: ")

                data, horario, linha = formatar_entrada(dataf, horariof, linhaf)
                resultado = arv.buscar_chegada(data, horario, linha)
                print(resultado)

            elif opc == 3:
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")
                linhaf = input("Digite a linha: ")

                data, horario, linha = formatar_entrada(dataf, horariof, linhaf)
                resultado = arv.remover_chegada(data, horario, linha)
                print(resultado)

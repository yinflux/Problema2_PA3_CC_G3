#Criando a classe principal da arvore de dados:
from datetime import datetime, timedelta
class Node:
    def __init__(self, data, horario, linha):
        self.data = data
        self.horario = horario
        self.linha = linha
        #Criando uma tupla(data, horario, linha), que em python ja faz a comparação lexicográfica
        self.chave = (data, horario, linha)

        self.esquerda = None
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
    
         # R3: PRÓXIMO(DATA, HORARIO) RETORNA DATA, HORÁRIO E LINHA DA PRIMEIRA CHEGADA A PARTIR DO INSTANTE INFORMADO, OU, "None"
    def proximo(self, data, horario):
       #Monta um alvo com linha vazia, para que a comparação com qualquer chegada >= (data, horario) seja verdadeira
       alvo = (data, horario, "")
       atual = self.raiz
       mlhrNO = None

       while atual:
            #Se a chave do no ocorreu no mesmo instante ou depois do instante informado, mlhrNO recebe o no atual para buscar por chegadas ainda mais próximas do instante informado
            if atual.chave >= alvo:
                mlhrNO = atual
                atual = (atual.esquerda)
            else:
                #O horario é anterior ao instante informado, entao busca por chegadas posteriores ao instante informado
                atual = (atual.direita)
       #Se encontrou algum no candidato, retorna os dados do mesmo, caso contrario retorna "None"
       if mlhrNO:
            return (mlhrNO.data, mlhrNO.horario, mlhrNO.linha)
        
       return None
        # R4: proximo_da_linha(data, horario, linha)
    def proximo_da_linha(self, data, horario, linha):
        if self.raiz is None:
            return None

        pilha = []
        atual = self.raiz
        instante_alvo = (data, horario)

        while pilha or atual:
            while atual:
                pilha.append(atual)
                # Só precisa descer à esquerda se o nó atual for >= ao instante buscado
                if (atual.data, atual.horario) >= instante_alvo:
                    atual = atual.esquerda
                else:
                    atual = None

            atual = pilha.pop()

            if (atual.data, atual.horario) >= instante_alvo and atual.linha == linha:
                return (atual.data, atual.horario)

            atual = atual.direita

        return None
    
         # R5: entre(data1, horario1, data2, horario2)
    def entre(self, data1, horario1, data2, horario2):
        instante_ini = (data1, horario1)
        instante_fim = (data2, horario2)

        if instante_ini > instante_fim or self.raiz is None:
            return []

        resultado = []  
        pilha = []
        atual = self.raiz

        while pilha or atual:
            while atual:
                pilha.append(atual)
                # Só explora a esquerda se ainda puder haver nós >= instante_ini
                if (atual.data, atual.horario) >= instante_ini:
                    atual = atual.esquerda
                else:
                    atual = None

            atual = pilha.pop()
            instante_atual = (atual.data, atual.horario)

            if instante_ini <= instante_atual <= instante_fim:
                resultado.append((atual.data, atual.horario, atual.linha))

            # Só explora a direita se o nó atual ainda for <= instante_fim
            if instante_atual <= instante_fim:
                atual = atual.direita
            else:
                atual = None

        return resultado

        # R7: ALTURA(ÁRVORE), RETORNA A ALTURA DA ÁRVORE DE CHEGADAS   
    def altura(self, no):
        if no is None:
            return 0
        else:
            altura_esquerda = self.altura(no.esquerda)
            altura_direita = self.altura(no.direita)
            return max(altura_esquerda, altura_direita) + 1

        # R8: espera_semanal(linha, data, horario, k)
    def espera_semanal(self, linha, data, horario, k):
        dt_base = datetime.strptime(data, "%Y-%m-%d")
        h_partes = horario.split(":")
        seg_consulta = int(h_partes[0]) * 3600 + int(h_partes[1]) * 60 + int(h_partes[2])

        respostas = []
        # Da semana mais antiga (k-1 semanas atrás) até a data informada (0 semanas atrás)
        for i in range(k - 1, -1, -1):
            data_alvo = (dt_base - timedelta(days=7 * i)).strftime("%Y-%m-%d")
            achado = self.proximo_da_linha(data_alvo, horario, linha)

            # Verifica se achou e se a chegada ocorreu NO MESMO DIA (data_alvo)
            if achado is not None and achado[0] == data_alvo:
                hc_partes = achado[1].split(":")
                seg_chegada = (
                    int(hc_partes[0]) * 3600
                    + int(hc_partes[1]) * 60
                    + int(hc_partes[2])
                )
                espera = seg_chegada - seg_consulta
                respostas.append(f"{data_alvo} {espera}")
            else:
                respostas.append(f"{data_alvo} NAOPASSOU")

        return respostas
        


# Formatar a entrada de dados para garantir a consistência do formato antes de registrar, buscar ou remover chegadas
def formatar_entrada(data, horario, linha):
  #Remove espaços e limita a 8 caracteres
  linha_formatada = linha.strip()[:8]

  #Tratamento da Data
  data_limpa = (
      data.strip()
      .replace('/', '')
      .replace('-', '')
      .replace('.', '')
      .replace(' ', '')
  )

  if len(data_limpa) == 8 and data_limpa.isdigit():
    #Digitou DDMMAAAA(: 10102000 -> 2000-10-10)
    if int(data_limpa[4:]) > 1900:
      dia, mes, ano = data_limpa[:2], data_limpa[2:4], data_limpa[4:]
      data_formatada = f'{ano}-{mes}-{dia}'
    #Digitou AAAAMMDD(20001010 -> 2000-10-10)
    else:
      ano, mes, dia = data_limpa[:4], data_limpa[4:6], data_limpa[6:]
      data_formatada = f'{ano}-{mes}-{dia}'
  else:
    #Caso tenha digitado assim (10/10/2000 ou 2000-10-10)
    partes_data = (
        data.strip().replace('/', '-').replace('.', '-').split('-')
    )
    if len(partes_data) == 3:
      if len(partes_data[0]) == 2 and len(partes_data[2]) == 4:
        dia, mes, ano = partes_data
        data_formatada = f'{ano}-{mes.zfill(2)}-{dia.zfill(2)}'
      else:
        ano, mes, dia = partes_data
        data_formatada = f'{ano}-{mes.zfill(2)}-{dia.zfill(2)}'
    else:
      data_formatada = data.strip()

  #Tratamento do Horário
  horario_limpo = horario.strip().replace(':', '').replace(' ', '')

  if len(horario_limpo) == 4 and horario_limpo.isdigit():
    #Digitou HHMM (1830 -> 18:30:00)
    hh, mm = horario_limpo[:2], horario_limpo[2:]
    horario_formatado = f'{hh}:{mm}:00'
  elif len(horario_limpo) == 6 and horario_limpo.isdigit():
    #Digitou HHMMSS (183000 -> 18:30:00)
    hh, mm, ss = horario_limpo[:2], horario_limpo[2:4], horario_limpo[4:]
    horario_formatado = f'{hh}:{mm}:{ss}'
  else:
    # Caso tenha digitado os dois pontos(18:30 ou 18:30:00)
    partes_horario = horario.strip().split(':')
    if len(partes_horario) == 2:
      hh, mm = partes_horario
      horario_formatado = f'{hh.zfill(2)}:{mm.zfill(2)}:00'
    elif len(partes_horario) == 3:
      hh, mm, ss = partes_horario
      horario_formatado = f'{hh.zfill(2)}:{mm.zfill(2)}:{ss.zfill(2)}'
    else:
      horario_formatado = horario.strip()

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

#1° versão do sistema(Problema 2 – A que horas passa o próximo ônibus?)
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
        self.altura = 1
#Craindo a classe ArvoreB que irá receber os principais comandos de inserir, remover, buscar
class ArvoreB:
    def __init__(self):
        self.raiz = None
    
    #Função para obter a altura do nó
    def ob_altura(self, no):
        if no is None:
            return 0
        return no.altura
    
    #Função para atualizar a altura de cada nó da arvore 
    def atl_altura(self, no):
        if no:
            no.altura = 1 + max(self.ob_altura(no.esquerda), self.ob_altura(no.direita))
    
    #Função que define o fator de balanceamento(ou seja faz a subtração da altura do nó da esquerda pela altura do nó da direita)
    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.ob_altura(no.esquerda) - self.ob_altura(no.direita)
    
    #Rotação à direita quando o lado da esquerda(altura) é maior que 1  
    def rotacao_dir(self , z):
        y = z.esquerda
        t3 = y.direita
       
        y.direita = z
        z.esquerda = t3
       
        self.atl_altura(z)
        self.atl_altura(y)
       
        return y
    
    #Rotação à esquerda quando o lado da direita(altura) é menor que -1   
    def rotacao_esq(self , z):
        y = z.direita
        t2 = y.esquerda
       
        y.esquerda = z
        z.direita = t2
       
        self.atl_altura(z)
        self.atl_altura(y)
       
        return y
    
    #Função mais importante da nossa AVL - Faz o rebalanceamento se estiver um lado maior que o outro, além de fazer as rotações duplas(quando é necessário fazer uma rotação a esquerda, para fazer uma rotação a direita. por exemplo)
    def rebalancear(self, z):
        self.atl_altura(z)
        fb = self.fator_balanceamento(z)
        
        if fb > 1:
            if self.fator_balanceamento(z.esquerda) < 0:
                z.esquerda = self.rotacao_esq(z.esquerda)
            return self.rotacao_dir(z)
            
        if fb < -1:
            if self.fator_balanceamento(z.direita) > 0:
                z.direita = self.rotacao_dir(z.direita)
            return self.rotacao_esq(z)
        return z
       
    #R1: registrar_chegada(data, horario, linha)    
    def registrar_chegada(self, data, horario, linha):
        #Inserindo uma nova chegada, regc recebe os dados necessários
        regc , resultado = self.registrar_recurs(self.raiz,data,horario,linha)
        self.raiz = regc
        return resultado
    
    def registrar_recurs(self, no, data, horario, linha):
        #Caso não tenha nenhum dado na raiz, regc passa a ser raiz
        if no is None:
            return Node(data, horario, linha), "OK"
        chave_nova = (data, horario, linha)

        #Se a chave(tupla) de chave_nova for igual a chave atual, retorna "DUPLICADO"
        if chave_nova == no.chave:
            return no, "DUPLICADO"
        #Recursivamente confere se chave_nova é menor que o nó atual, se sim, se esquerda de atual estiver livre, chave_nova entra nela, se esquerda n estiver vazia, atual é igual ao mesmo dado olhado na conferência anterior, o que isso faz com que recursivamente se "crie" uma subarvore a esquerda, até que a esquerda de atual esteja livre.
        if chave_nova < no.chave:
            no.esquerda, resultado = self.registrar_recurs(no.esquerda, data, horario, linha)
        else:
        #Mesma lógica da esquerda, porém nesse caso agora para direita, ou seja, para valores maior que o nó atual
            no.direita, resultado = self.registrar_recurs(no.direita, data, horario, linha)

        if resultado == "DUPLICADO":
            return no, "DUPLICADO"

        #Ajuste da altura e rebalanceamento do nó atual(tipico de uma AVL)
        no_rebalanceado = self.rebalancear(no)
        
        return no_rebalanceado, resultado
    
   # R6: remover_chegada(data, horario, linha)
    def remover_chegada(self, data, horario, linha):
        chave_alvo = (data, horario, linha)
        self.raiz, resultado = self.remover_recurs(self.raiz, chave_alvo)
        return resultado
    def remover_recurs(self, no, chave_alvo):
        # Caso 1: chegou em None e não encontrou a chegada
        if no is None:
            return None, "NAO"
        # Busca recursivamente pela chave_alvo na subárvore esquerda ou direita
        if chave_alvo < no.chave:
            no.esquerda, resultado = self.remover_recurs(no.esquerda, chave_alvo)
        elif chave_alvo > no.chave:
            no.direita, resultado = self.remover_recurs(no.direita, chave_alvo)
        else:
            # Achou o nó a ser removido!
            # Caso 1: Nó com 0 ou 1 filho
            if no.esquerda is None:
                return no.direita, "OK"
            if no.direita is None:
                return no.esquerda, "OK"
        # Caso 2: Nó com 2 filhos -> substitui pelo sucessor (menor da subárvore direita)
            suc = no.direita
            while suc.esquerda is not None:
                suc = suc.esquerda

            # Copia os dados do sucessor para o nó atual
            no.chave = suc.chave
            no.data = suc.data
            no.horario = suc.horario
            no.linha = suc.linha

            # Remove fisicamente o sucessor da subárvore direita
            no.direita, _ = self.remover_recurs(no.direita, suc.chave)
            resultado = "OK"

        # Se a chave não existia na árvore, não rebalanceia
        if resultado == "NAO":
            return no, "NAO"

        # Atualiza a altura e rebalanceia o nó atual na volta da recursão (AVL)
        no_rebalanceado = self.rebalancear(no)
        return no_rebalanceado, resultado
       
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
       #Se encontrou algum no candidato, retorna os dados do mesmo, caso contrario retorna "Nenhum"
       if mlhrNO:
            return f"{mlhrNO.data} {mlhrNO.horario} {mlhrNO.linha}"
       
       return "NENHUM"
    # R4: proximo_da_linha(data, horario, linha)
    def proximo_da_linha(self, data, horario, linha):
        if self.raiz is None:
            return "NENHUM"

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
                return f"{atual.data} {atual.horario}"

            atual = atual.direita

        return "NENHUM"
   
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

    # R7: ALTURA DA ÁRVORE, RETORNA A ALTURA DA ÁRVORE DE CHEGADAS
    def altura(self, no=None):
        # Na AVL, a altura já fica guardada e atualizada na raiz em O(1)
        if no is None:
            return self.ob_altura(self.raiz)
        return self.ob_altura(no)
       

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
            if achado !="NENHUM":
                data_encontrada, hora_encontrada = achado.split(" ")
                if data_encontrada == data_alvo:
                 hc_partes = hora_encontrada.split(":")
                 seg_chegada = (
                 int(hc_partes[0]) * 3600
                  + int(hc_partes[1]) * 60
                  + int(hc_partes[2])
                 )
                 espera = seg_chegada - seg_consulta
                 respostas.append(f"{data_alvo} {espera}")
                else:
                 respostas.append(f"{data_alvo} NAOPASSOU")
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

        opc = -1
        arv = ArvoreB()

        while opc != 0:
            print("1 - Registrar chegada")
            print("2 - Buscar chegada")
            print("3 - Remover chegada")
            print("4 - Exibir altura da árvore")
            print("5 - Buscar próximo registro")    
            print("6 - Buscar próximo registro da linha")
            print("7 - Buscar chegadas entre dois instantes")
            print("8 - Espera semanal")
            print("0 - Sair")
           
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

            elif opc == 4:
                            altura = arv.altura(arv.raiz)
                            print(f"A altura da árvore é: {altura}")

            elif opc == 5:
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")

                data, horario, _ = formatar_entrada(dataf, horariof, "")
                proximo_registro = arv.proximo(data, horario)

                print(proximo_registro)
                   
            elif opc == 6:
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")
                linhaf = input("Digite a linha: ")

                data, horario, linha = formatar_entrada(dataf, horariof, linhaf)
                proximo_registro_linha = arv.proximo_da_linha(data, horario, linha)

                print(proximo_registro_linha)

            elif opc == 7:
                data1f = input("Digite a data inicial: ")
                horario1f = input("Digite o horário inicial: ")
                data2f = input("Digite a data final: ")
                horario2f = input("Digite o horário final: ")

                data1, horario1, _ = formatar_entrada(data1f, horario1f, "")
                data2, horario2, _ = formatar_entrada(data2f, horario2f, "")

                registros_entre = arv.entre(data1, horario1, data2, horario2)
               
                if registros_entre:
                    for registro in registros_entre:
                        print(f"{registro[0]} {registro[1]} {registro[2]}")
                else:
                    pass

            elif opc == 8:
                linhaf = input("Digite a linha: ")
                dataf = input("Digite a data: ")
                horariof = input("Digite o horário: ")
                k = int(input("Digite o número de semanas (k): "))

                data, horario, linha = formatar_entrada(dataf, horariof, linhaf)
                resultados_espera = arv.espera_semanal(linha, data, horario, k)
                print("Resultados da espera semanal:")
                for resultado in resultados_espera:
                    print(resultado)

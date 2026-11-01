# Problema2_PA3_CC_G3
Projeto Aplicado III - Ciência da Computação

Problema 2 - A que horas passa o próximo ônibus?
Sistema de Registro, Busca e gerenciamento de horários de ônibus.

# Ambiente de Programação
Linguagem: Python

Versão da Linguagem: 3.13

Sistema Operacional de Execução: Windows 10

# FASE 2 - Medição do sistema(testes)
Para testar o sistema, recomendamos colocar os arquivos de carga na pasta fase2 -> Problema2_PA3_CC_G3/fase2
o arquivo principal dessa fase é metricas.py, é práticamente uma cópia da função principal do sistema.py da fase1 e posteriormente terá o sistema.py da fase3, porém no metricas.py temos a função processar_entradas() que a partir de um arquivo de entradas consegue gerar os resultados de cada operação, e o tempo que é levado para processar cada uma delas.

Para a realização dos testes:
Abra um terminal de cmd(prompt de comando) no VS code, ou na IDE que esteja utilizando (se houver a opção) e escreva os seguintes comandos:

Para gerar um arquivo .txt de saidas de cada função coloque: ex: py metricas.py < carga_embaralhada_1000.txt > saida.txt | esse comando tem como print no terminal apenas o bloco de medição, com os tempos totais, as saidas de cada função fica na saida.txt
Agora para apenas poder ver os tempos totais e medição do sistema: ex: py metricas.py < carga_embaralhada_1000.txt > NUL

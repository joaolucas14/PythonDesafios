from ex116.lib.interface import *
from ex116.lib.dados import *

arq = 'time.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver os jogadores do time', 'Cadastrar um novo jogador', 'Encerrar o programa'])
    if resposta ==1:
        lerArquivo(arq)
    elif resposta ==2:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        gols = int(input('Gols: '))
        cadastrar(arq, nome, idade, gols)
    elif resposta == 3:
        print('\033[33mSaindo do programa até logo!\033[m')
        break
    else:
        print('Valor inválido')
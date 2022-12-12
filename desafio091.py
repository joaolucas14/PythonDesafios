from random import randint; from time import sleep; from operator import itemgetter
jogadores = {'jogador01': randint(1, 6), 'jogador02': randint(1, 6),
             'jogador03': randint(1, 6), 'jogador04': randint(1, 6)}
print('VALORES SORTEADOS')
ranking = []
for k, v in jogadores.items():
    print(f'{k} com {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key= itemgetter(1), reverse= True)
print('RANKING DOS JOGADORES: ')
for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0]} com {v[1]}')
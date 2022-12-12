from time import sleep
from random import randint
sorteio = []
lista = []
print('-='*30)
print('MEGA SENA')
print('-='*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for j in range(0, jogos):
    while len(sorteio) <6:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
        else:
            num = randint(1, 60)
    sorteio.sort()
    lista.append(sorteio[:])
    sorteio.clear()
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
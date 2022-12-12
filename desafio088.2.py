from random import randint
from time import sleep
sorteio = []
print('-='*30)
jogos = int(input('Informe quantos jogos quer fazer: '))
print('-='*30)
for s in range(0, jogos):
    for n in range(0,6):
        while True:
            num = randint(1, 60)
            if num not in sorteio:
                sorteio.append(num)
                break
    sorteio.sort()
    print(f'Jogo {s + 1}: {sorteio}')
    sleep(2)
    sorteio.clear()

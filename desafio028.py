from random import randint
from time import sleep
n = randint(0, 5)
n1 = int(input('Escolha um número: '))
print('PROCESSANDO...')
sleep(3)
print('Seu número escolhido foi {}, número da maquina foi {}'.format(n1, n))
if n == n1:
    print('Você ganhou!!!')
else:
    print('Você perdeu!!!')

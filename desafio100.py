from random import randint
numeros = []
pars = []
def lista():
    print('Sorteando 5 números: ',end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
    print('Pronto!')
def spar():

    for c in numeros:
        if c % 2 == 0:
            pars.append(c)
    print(f'Somando os valores pares: {pars} temos {sum(pars)}')


lista()
spar()
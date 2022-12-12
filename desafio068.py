from random import randint
v = 0
r2 =''
while True:
    n = int(input('Digite um número: '))
    pi = input('Par ou Ímpar? [P/I]')
    n2 = randint(0, 10)
    r = n + n2
    if r % 2 == 0:
        r2 = 'Par'
    else:
        r2 = 'Ímpar'
    print(f'Você digitou {n}, e o computador {n2}, total de {r} deu {r2}')
    if r % 2 == 0 and pi in 'Pp':
        v += 1
        print('Vcoê ganhou! Vamos jogar novamente')
    elif r % 2 != 0 and pi in 'Ii':
            v += 1
            print('Vcoê ganhou! Vamos jogar novamente')
    else:
        break
print(f'Você perdeu! total de vitorias seguida {v}')

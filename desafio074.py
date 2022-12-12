from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10), )
print('Os valores sorteados foram: ',end='')
for c in n:
    print(c,end=' ')
print(f'\nO maior valor foi {max(n)}')
print(f'E o menor valor foi de {min(n)}')
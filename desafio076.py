listagem = ('Lápiz', 1.50, 'Caneta', 2.00, 'Caderno', 10.00, 'Mochila', 120.00)
print('-='*20)
print(f'{"LISTA DE PREÇOS":^40}')
print('-='*20)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20}',end='')
    else:
        print(f'R${listagem[c]:>7}')
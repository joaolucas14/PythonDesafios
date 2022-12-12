par = 0
n = (int(input('Informe um número: ')),
     int(input('Informe um número: ')),
     int(input('Informe um número: ')),
     int(input('Informe um número: ')))
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu primeiro na posição {n.index(3)+1}.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
for c in n:
    if c % 2 == 0:
        par += 1
print(f'Foram digitados {par} valores pares.')

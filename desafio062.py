p1 = int(input('Informe o primeiro termo: '))
ra = int(input('Informe a razão: '))
c1 = 1
c2 = 1
x = 10
print(p1, end=' ')
while c1 < 10:
    pa = p1 + ra
    p1 = pa
    print(pa, end=' ')
    c1 = c1 + 1
x = int(input('\nQuer saber mais quantos termos? '))
while not x == 0:
    pa = p1 + ra
    p1 = pa
    print(pa, end=' ')
    x = x - 1
    if x == 0:
        x = int(input('\nQuer saber mais quantos termos? '))
print('Fim do programa!')

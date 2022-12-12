def area(l, c):
    a = l * c
    print(f'A área do terreno de {l}X{c} é de {a}m2')


print('Controle de terreno')
print('-='*30)
l = float(input('Largura(M): '))
c = float(input('Comprimento(M)'))
area(l, c)
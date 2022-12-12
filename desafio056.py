maior = 0
m1 = 0
me20 = 0
for c in range(0,4):
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo [M/F]')
    m1 = m1 + idade
    if sexo.lower() == 'm' and idade > maior:
        maior = idade
        maisv = nome
    if sexo.lower() == 'f' and idade < 20:
        me20 = me20 + 1
m2 = m1 / 4
print('A média de idade do grupo é de: {}'.format(m2))
print('O {}, é o homem mais velho'.format(maisv))
print('Tem {} mulheres menores de 20 anos.'.format(me20))
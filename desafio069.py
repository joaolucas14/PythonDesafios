f20 = h= p18= 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Sexo: [M/F]').strip().lower()[0]
    cont = ' '
    while cont not in 's/n':
        cont = input('Quer continuar? [S/N]').strip().lower()[0]
    if idade >= 18:
        p18 += 1
    if sexo in 'm':
        h += 1
    if sexo in 'f' and idade <= 20:
        f20 += 1
    if cont =='n':
        break
print(f'''Quantidade de pessoas maiores de 18: {p18}
Quantidade de homens: {h}
Quantidade de mulheres com menos de 20 anos: {f20}''')

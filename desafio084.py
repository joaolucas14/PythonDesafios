pessoas = []
dados = []
maiorp = menorp =  0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if maiorp < dados[1]:
            maiorp = dados[1]
        if menorp > dados[1]:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break

print('-='*30)
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi de {maiorp} KG de: ', end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {menorp} KG de: ', end='')
for p in pessoas:
    if p[1] == menorp:
       print(f'[{p[0]}]',end='')
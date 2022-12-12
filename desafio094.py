dados = {}
pessoas = []
totid = 0
while True:
    dados.clear()
    dados['nome'] = input('Qual é o seu nome: ')
    while True:
        dados['sexo'] = input('Qual é o seu sexo: [M/F]').upper()
        if dados['sexo'] in 'MF':
            break
        else:
            print('Valor inválido!, digite novamente.')
    dados['idade'] = int(input('Informe sua idade: '))
    totid += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N]').upper()
        if resp in 'SN':
            break
        else:
            print('Valor inválido!, digite novamente.')
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade é de {totid / len(pessoas):.2f}')
print('Mulheres cadastradas: ',end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(c['nome'],end=' ')
print('\nLista de pessoas que estão acima da média de idade: ')
for c in pessoas:
    if c['idade'] >= (totid / len(pessoas)):
        for k, v in dados.items():
            print(f'{k} = {v}', end=' ')
        print()
print('Fim do programa!')
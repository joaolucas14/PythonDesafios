lista = []
cont = 0
while True:
    lista.append(int(input('Informe um número: ')))
    cont += 1
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break
print(f'Foram digitados: {len(lista)} números')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('Não foi encontrado nenhum valor 5')

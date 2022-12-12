cont = 's'
t = m1000 = 0
menor = 100000000
while cont != 'n':
    nome = input('Informe o nome do produto: ')
    preço = float(input('Informe o preço do produto: '))
    cont = input('Quer continuar? [S/N]').lower()
    t += preço
    if preço > 1000:
        m1000 += 1
    if preço < menor:
        nomem = nome
        menor = preço
print(f'Valor total gasto: R$ {t:.2f}')
print(f'Quantidade de produtos acima de R$ 1.000: {m1000}')
print(f'Nome do produto mais barato: {nomem} que custa R$ {menor:.2f}')

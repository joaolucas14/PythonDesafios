dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
preço = (60 * dias) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(preço))
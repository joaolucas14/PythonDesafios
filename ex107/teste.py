from ex107 import moedas

num = float(input('Digite o preço R$ '))
print(f'A metade de R${num} é {moedas.metade(num)}')
print(f'O dobro de R${num} é {moedas.dobro(num)}')
print(f'Aumentando 10% temos: R${moedas.aumento(num)}')
print(f'Reduzindo 13% temos: R${moedas.redução(num)}')

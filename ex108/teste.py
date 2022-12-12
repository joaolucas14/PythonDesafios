from ex108 import moedas

num = float(input('Digite o preço R$ '))
print(f'A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}')
print(f'Aumentando 10% temos: {moedas.moeda(moedas.aumento(num))}')
print(f'Reduzindo 13% temos: {moedas.moeda(moedas.redução(num))}')

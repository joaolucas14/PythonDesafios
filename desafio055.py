maior = 0
menor = 100000
for c in  range(0,5):
    peso = int(input('Informe seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi de Kg {}, e o menor foi de Kg {}'.format(maior, menor))



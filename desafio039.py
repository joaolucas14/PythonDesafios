idade = int(input('Informe sua idade: '))
if idade > 18:
    print('Você já se alistou')
elif idade < 18:
    print('Você se alistará em {}'.format(18 - idade))
else:
    print('Você se alistará esse ano.')

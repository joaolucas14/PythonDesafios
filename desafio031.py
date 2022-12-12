km = float(input('Informe a quilometragem de sua viagem: '))
if km <= 200:
    p = km * 0.50
else:
    p = km * 0.45
print('O valor de sua viagem é de R${:.2f}'.format(p))

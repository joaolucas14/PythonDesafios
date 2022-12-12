from math import hypot
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = hypot(co, ca)
print('O valor da hipotenusa é de {:.2f}'.format(h))
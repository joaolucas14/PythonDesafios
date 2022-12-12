a = int(input('Informe um número:'))
b = int(input('Informe um número:'))
c = int(input('Informe um número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
   maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}, e o menor foi {}'.format(maior, menor))


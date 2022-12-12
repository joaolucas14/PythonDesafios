op = 's'
c = 0
m1 = 0
maior = 0
menor = 1000000000
while op in 'Ss':
    n = int(input('Informe um número: '))
    c = c +1
    m1 = m1 + n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    op = input('Quer continuar? [S/N]')
m2 = float(m1 / c)
print('A média foi de {:.2f}, maior número {}, menor número {}'.format(m2, maior, menor))

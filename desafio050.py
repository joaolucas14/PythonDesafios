s = 0
for c in range(0, 6):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos números pares foi de: {}'.format(s))

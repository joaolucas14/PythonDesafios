n = int(input('Informe um número: '))
r = 0
for c in range(0, 11):
    r = n * c
    print('{} X {:2} = {}'.format(c, n, r))

n = int(input('Informe um número: '))
r = int(input('Informe a razão: '))
print(n ,end='')
for c in range(0,10):
    pa = n + r
    n = pa
    print(',',pa, end='')
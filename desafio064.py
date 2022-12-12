n = 0
s = 0
c = 0
while not n == 999:
    n = int(input('Informe um número: '))
    if n != 999:
        c = c +1
        s = s + n
print('Foram digitados {} números, e a soma é de {}'.format(c, s))

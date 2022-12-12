from time import sleep
def cont(i, f, p):
    print(f'Contagem de {i} até {f} com passo {p}')
    if p == 0:
        if i > f:
            for c in range(i, f-1, -1):
                print(c, end=' ')
            print()
        else:
            for c in range(i, f+1, 1):
                print(c, end=' ')
            print()
    else:
        if i > f:
            for c in range(i, f-1, p):
                print(c, end=' ')
            print()
        else:
            for c in range(i, f+1, p):
                print(c, end=' ')
            print()


cont (0, 10, 1)
cont(10, 0, -2)
i = int(input('Informe o valor para i: '))
f = int(input('Informe o valor para f: '))
p = int(input('Informe o valor para p: '))
cont(i, f, p)

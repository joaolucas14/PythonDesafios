def metade(n=0):
    resp = n / 2
    return resp


def dobro(n=0):
    resp = n * 2
    return resp

def aumento(n=0,t=0):
    resp = n + (n * t/100)
    return resp

def redução(n=0, t=0):
    resp= n - (n * t/100)
    return resp


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, ta, td):
    print('-='*15)
    print('Resumo do valor'.center(30))
    print('-='*15)
    print(f'Preco analisado {moeda(n)}')
    print(f'A metade de {moeda(n)} é {moeda(metade(n))}')
    print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
    au = aumento(n,ta)
    print(f'Aumentando {ta}% temos: {moeda(au)}')
    re = redução(n, td)
    print(f'Reduzindo {td}% temos: {moeda(re)}')
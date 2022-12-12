def metade(n=0, f=False):
    resp = n / 2
    if f == True:
      return moeda(resp)
    else:
        return resp


def dobro(n=0, f=False):
    resp = n * 2
    if f == True:
        return moeda(resp)
    else:
        return resp

def aumento(n=0, f=False):
    resp = n * 1.10
    if f == True:
        return moeda(resp)
    else:
        return resp

def redução(n=0, f=False):
    resp= n - n*0.13
    if f == True:
        return moeda(resp)
    else:
        return resp


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

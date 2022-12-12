def voto(a):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - a
    if idade < 16:
        r = f'Com {idade} anos: Não vota'
    elif idade < 65 and idade >= 18:
        r = f'Com {idade} anos: Voto obrigatório'
    else:
        r = f'Com {idade} anos: Voto opcional'
    print(r)


anon = int(input('Informe seu ano de nascimento: '))
voto(anon)

dic = {}
def nota(lst, sit=False):
    dic['total'] = len(lst)
    dic['maior'] = max(lst)
    dic['menor'] = min(lst)
    dic['média'] = sum(lst) / len(lst)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        elif dic['média'] >=5:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    print(dic)

boletim = (5.5, 9.5, 10, 6.5)
nota(boletim)
boletim = (7, 8, 8)
nota(boletim, sit=True)
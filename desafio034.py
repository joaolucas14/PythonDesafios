sal = float(input('Informe seu salário: '))
if sal <= 1250:
    nsal =  sal * 0.15
    nsal2 = sal + nsal
else:
    nsal = sal * 0.10
    nsal2 = sal + nsal
print('O seu novo salário é de R${:.2f}'.format(nsal2))
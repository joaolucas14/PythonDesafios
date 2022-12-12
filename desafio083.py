pd = pe = 0
expressao = input('Informe sua expressão: ')
pd = expressao.count('(')
pe = expressao.count(')')
if pd == pe:
    print('Expressão válida!')
else:
    print('Sua expressão está errada!')
n1 = int(input('Informe sua nota: '))
n2 = int(input('Informe sua nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mVocê está reprovado\033[m')
elif 5 <= m < 7:
    print('\033[33mVocê está de recuperação\033[m')
else:
    print('\033[32mVocê está aprovado parabéns!\033[m')
print('Sua média foi de {:.2f}'.format(m))

m21 = 0
for c in range(0, 7):
    ano = int(input('Informe seu ano de nascimento: '))
    if 2022 - ano >= 21:
        m21 = m21 + 1
print('{} pessoas são maiores de idade, {} são menores'.format(m21, 7 - m21))

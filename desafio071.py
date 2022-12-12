n = int(input('Informe o valor que quer sacar: '))
c50 = n //50
c20 = (n - c50 * 50) // 20
c10 = ((n - c50 * 50) - c20 * 20) //10
c1 = (((n - c50 * 50) - c20 * 20) - c10 * 10) // 1
print(f'Total de {c50} cédulas de R$ 50')
print(f'Total de {c20} cédulas de R$ 20')
print(f'Total de {c10} cédulas de R$ 10')
print(f'Total de {c1} cédulas de R$ 1')
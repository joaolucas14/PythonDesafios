nt = []
ni = []
np = []
while True:
    n = int(input('Informe um número: '))
    nt.append(n)
    if n % 2 ==0:
        np.append(n)
    else:
        ni.append(n)
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break
print(f'Todos os números digitados {nt}')
print(f'Todos os números pares digitados {np}')
print(f'Todos os números ímpares digitados {ni}')

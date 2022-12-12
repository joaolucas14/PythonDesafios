numeros = [[], []]
for c in range(0, 7):
    valor = int(input('Informe um número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Numeros pares:  {numeros[0]}')
print(f'Numeros ímpares: {numeros[1]}')

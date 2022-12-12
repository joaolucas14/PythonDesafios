numeros = []
opcao = 's'
while not opcao == 'n':
    n = int(input('Informe um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = input('Deseja continuar? [S/N]').lower().strip()
print(f'Os valores digitados em ordem crescente são: \n {sorted(numeros)}')
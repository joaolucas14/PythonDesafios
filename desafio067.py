while True:
    n = int(input('Informe um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {c*n}')
print('Fim do programa!')

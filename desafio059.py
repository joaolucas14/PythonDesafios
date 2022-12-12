n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número:'))
op = 0
while not op == 5:
    op = int(input(''' [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Sair do programa '''))
    if op == 1:
        s = n1 + n2
        print('A soma de {} com {} é igual a : {}'.format(n1, n2, s))
    if op == 2:
        m = n1 * n2
        print('A multiplicação de {} com {} é igual a : {}'.format(n1, n2, m))
    if op == 3:
        if n1 >= n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    if op == 4:
        n1 = int(input('Informe outro número: '))
        n2 = int(input('Informe outro número: '))
print('Fim do programa!')
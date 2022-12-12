def leiaint(n1):
    ok =False
    valor = 0
    while True:
        n = input(n1)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}')
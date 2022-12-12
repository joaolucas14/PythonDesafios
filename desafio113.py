def leiaint(n1):
    while True:
        try:
            n = int(input(n1))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except InterruptedError:
            print('\n\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return n


def leiafloat(n2):
    while True:
        try:
            n = float(input(n2))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return n


i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i}\nO valor float digitado foi {f}')
print('Volte sempre!')
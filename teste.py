def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('Valor inválido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar um valor')
            return 0
        return n


n = inteiro('Informe um número inteiro: ')
print(n)
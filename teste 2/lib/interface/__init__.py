def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mValor inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não inserir o valor\033[m')
            return 0
        else:
            return n

def linha(tam =42):
    print('-'* tam)


def cabeçalho (msg):
    linha()
    print(msg.center(42))
    linha()

def menu(lst):
    cabeçalho('DADOS DO TIME')
    c =1
    for item in lst:
        print(f'\033[33m{c}\033[m - \033[35m{item}\033[m')
        c += 1
    linha()
    op = leiaint('\033[32mSua opção: \033[m')
    return op
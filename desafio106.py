from time import sleep
def pyhelp(msg):
    print('\033[46m-=' * 20)
    print(f'Acessando o manual do comando {msg}')
    print('-=' * 20)
    sleep(1)
    print('\033[m')
    print('\033[47m')
    print(help(msg))
    print('\033[m')

while True:
    print('\033[42m-=' * 13)
    print('Sistema de ajuda pyhelp!')
    print('-='*13)
    print('\033[m')
    op = input('Função ou Biblioteca > ').lower()
    if op == 'fim':
        print('\033[41m-=' * 5)
        print('Até logo')
        print('-=' * 5)
        print('\033[m')
        break
    pyhelp(op)

n = int(input('Digite um número inteiro: '))
print(''''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para  Octal
[ 3 ] Converter para  Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para \033[33mbinário\033[m é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para \033[33moctal\033[m é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para \033[33mhexadecimal\033[m é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mOpção invalida\033[m')
nome = input('Informe seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
n1 = int(nome.count(' '))
n2 = int(len(nome))
n3 = n2 - n1
print('Seu nome tem {} letras'.format(n3))
div = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(div[0], len(div[0])))

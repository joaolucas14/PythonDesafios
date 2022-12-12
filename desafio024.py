cidade = input('Informe o nome da sua cidade: ').strit()
div = cidade.split()
print('Sua cidade começa com Santo? {}'.format('santo'in div[0].lower()))

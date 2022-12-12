def leiadinheiro(n):
    valido = False
    while not valido:
        entrada = str(input(n)).replace(',','.')
        if entrada.isalpha() or entrada.strip()=='':
            print(f'\033[31mERRO! {entrada} é um preço inválido!\033[m')
        else:
            valido= True
            return float(entrada)
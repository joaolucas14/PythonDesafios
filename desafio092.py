from datetime import datetime
nome = input('Informe o seu nome: ')
datan = int(input('Informe seu ano de nascimento: '))
idade = datetime.now().year - datan
carteira = int(input('Carteira de trabalho: (0 não tem)'))
trabalhador = {'nome': nome, 'idade': idade, 'ctps': carteira}
if carteira == 0:
    for k, v in trabalhador.items():
        print(f'{k} tem o valor {v}')
else:
    contrato = int(input('Ano de contratação: '))
    trabalhador['contratação'] = contrato
    trabalhador['salário'] = float(input('Informe seu salário: '))
    apo = (35 - (datetime.now().year - contrato)) + idade
    trabalhador['aposentadoria'] = apo
    for k, v in trabalhador.items():
        print(f'{k} tem o valor {v}')

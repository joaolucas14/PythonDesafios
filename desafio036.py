casa = int(input('Informe o valor da casa: '))
sal = int(input('Informe seu salário:'))
ano = int(input('Informe em quantos anos quer pagar a casa:'))
fi = casa / (ano * 12)
p30 = sal * 0.30
if p30 <= fi:
    print('\033[31mVocê não poderá financiar essa casa.\033[m')
else:
    print('{}Parábens financiamento aceito! {} \n Suas parcelas serão de R${:.2f} por {} anos. '.format('\033[33m',
                                                                                                        '\033[m', fi,
                                                                                                        ano))

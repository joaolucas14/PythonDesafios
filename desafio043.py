p = int(input('Informe seu peso: '))
alt = float(input('Informe sua altura: '))
imc = float(p / (alt**2))
if imc < 18.5:
    print('Seu imc é {:.2f}. \033[37mAbaixo do peso.\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.2f}. \033[32mPeso ideal.\033[m'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.2f}. \033[33mSobrepeso.\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é {:.2f}. \033[35mObesidade.\033[m'.format(imc))
else:
    print('Seu imc é {:.2f}. \033[31mObesidade mórbida.\033[m'.format(imc))

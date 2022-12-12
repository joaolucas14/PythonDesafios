vel = int(input('Informe sua velocidade: '))
if vel <= 80:
    print('Você não foi multado.')
else:
    multa1 = vel - 80
    multa2 = multa1 * 7
    print('Você estava a {}KM/h e foi multado no valor de R${:.2f}'.format(vel, multa2))

r1 = int(input('Informe sua reta: '))
r2 = int(input('Informe sua reta: '))
r3 = int(input('Informe sua reta: '))
if r1 + r2 > r3 and r2 + r1 > r3 and r3 + r1 > r2 and r1 + r3 > r2 and r2 + r3 > r1 and r3 + r2 > r1:
    print('Sua reta pode formar um triângulo,', end=' ')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Essas retas não podem formar um triângulo')
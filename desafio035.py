r1 = int(input('Informe o tamanho de sua reta: '))
r2 = int(input('Informe o tamanho de sua reta: '))
r3 = int(input('Informe o tamanho de sua reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r2 + r1 > r3 and r3 + r1 > r2 and r3 + r2 > r1:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')

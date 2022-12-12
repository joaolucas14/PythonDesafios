import math
a = int(input('Informe um ângulo: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo {} tem o seno de {:.2f}, cosseno de {:.2f}, e a tangente de {:.2f}'.format(a, seno, cos, tan))


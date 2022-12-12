from random import randint
res = 0
tent = 0
cpu = randint(1, 10)
while not res == cpu:
    res = int(input('Qual é o seu palpite: '))
    tent = tent + 1
    if res > cpu:
        print('Menos... Tente novamente')
    if res < cpu:
        print('Mais ... Tente novamente')
print('O número escolhido era {}'.format(cpu))
print('Você acertou em {} tentativas parabens'.format(tent))

from random import randint
from time import sleep
print('\033[35m-_-_-\033[m'*5)
print('         \033[36mJOKEMPÔ\033[m')
print('\033[35m-_-_-\033[m'*5)
escolha = int(input('Escolha: Pedra[1]/ Papel[2]/ Tesoura[3] \n'))
cpu = randint(1,3)
if cpu == 1:
    maq = 'Pedra'
elif cpu == 2:
    maq = 'papel'
else:
    maq = 'Tesoura'
if escolha == 1:
    pe = 'Pedra'
elif escolha == 2:
    pe = 'papel'
else:
    pe = 'Tesoura'
print('\033[33mAguardando resultado\033[m')
sleep(1)
print('Você escolheu {}, e a CPU {}'.format(pe, maq))
if escolha == cpu:
    print('\033[33mJogue novamente!\033[m')
elif escolha == 1 and cpu ==2:
    print('\033[31mA CPU venceu!!!\033[m')
elif escolha == 1 and cpu ==3:
    print('\033[32mVocê venceu!!!. Parábens\033[m')
elif escolha == 2 and cpu ==3:
    print('\033[31mA CPU venceu!!!')
elif escolha == 2 and cpu ==1:
    print('\033[32mVocê venceu!!!. Parábens\033[m')
elif escolha == 3 and cpu ==1:
    print('\033[31mA CPU venceu!!!')
elif escolha == 3 and cpu ==2:
    print('\033[32mVocê venceu!!!. Parábens\033[m')

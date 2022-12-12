jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    tot = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida{c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = input('Quer continuar? [S/N]').upper()
    if resp == 'N':
        print('-='*30)
        break
    print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para)'))
    if busca == 999:
        break
    print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
    for i, g in enumerate(time[busca]['gols']):
        print(f'   No jogo {i} fez {g} gols. ')
    print('-'*30)
print('Volte sempre')
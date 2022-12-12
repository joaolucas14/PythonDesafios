jogador = {}
gol = []
jogador['nome'] = input('Qual é o seu nome: ').title()
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou?'))
for c in range(0, jogos):
    gol.append(int(input(f'Quantos gols no jogo {c+1}: ')))
tot = sum(gol)
print('-='*30)
print(f'{jogador["nome"]} jogou {jogos} jogos: ')
for i, c in enumerate(gol):
    print(f'Jogo {i +1}: {c} gols')
print(f'Total de {tot} gols!')

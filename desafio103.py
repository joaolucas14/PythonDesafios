def ficha(nome, gols=0):
    if nome == '':
        print(f'Jogador desconhecido fez {gols} gol(s) no campeonato.')
    else:
        print(f'Jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Informe seu nome: ').title()
gol = input('Quantidade de gols marcados: ')
if gol.strip() == '':
    ficha(n)
else:
    ficha(n, gol)

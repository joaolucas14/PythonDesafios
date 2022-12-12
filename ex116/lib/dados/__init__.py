from ex116.lib.interface import *
def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('\033[31mErro ao criar arquivo!\033[m')
    else:
        print(f'Arquivo {txt} criado com sucesso!')

def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('JOGADORES CADASTRADOS')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<20} {dado[1]:>3} Anos {dado[2]:>3} Gols')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0, gols=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mErro na abertura do  arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade};{gols}\n')
        except:
            print('\033[31mErro ao cadastrar os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()



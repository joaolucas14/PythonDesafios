from ex115.lib.interface  import *

def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')#ler um arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')#Se o arquivo não existir ele cria
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {txt} criado com sucesso!')


def lerArquivo(txt):
    try:
        a=open(txt,'rt')
    except:
        print('Houve algum ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()


aluno = {'nome': input('Nome: '), 'media': int(input('Média: '))}
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado!'
else:
    aluno['situação'] = 'Reprovado!'
for k, v in aluno.items():
    print(f'{k}: {v}')
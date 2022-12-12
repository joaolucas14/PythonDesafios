va = []
for c in range(0,5):
    va.append(int(input(f'Informe um valor para a posição {c}: ')))
print(f'O maior valor foi: {max(va)} na posição ', end='')
for p, v in enumerate(va):
    if v == max(va):
        print(p, ' ', end='')
print(f'\nO menor valor foi: {min(va)} na posição', end='')
for p, v in enumerate(va):
    if v ==min(va):
        print(p, ' ',end='')

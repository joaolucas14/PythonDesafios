p1 = int(input('Informe o primeiro termo: '))
ra = int(input('Informe a razão: '))
c = 1
print(p1, end='->')
while c < 10:
    pa = p1 + ra
    p1 = pa
    print(pa, end='->')
    c = c+1
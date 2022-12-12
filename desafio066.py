s = 0
c = 0
while True:
    n = int(input('Digite úm número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números, e a soma total é de {s}')
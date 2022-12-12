num = []
for c in range(0,5):
    n = int(input('Informe um número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                break
            pos += 1
print(f'Os valores em ordem são: {num}')
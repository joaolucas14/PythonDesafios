def fatorial(f,show):
    num = 1
    if show == True:
        for c in range(f, 0, -1):
            num *= c
            print(f'{c} X ', end='')
        print(f'= {num}')
    else:
        for c in range(f, 0, -1):
            num *= c
        print(num)


fatorial(5, show = True)
fatorial(6, show = False)
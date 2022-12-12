def maior(*n):
    s = max(n)
    for c in n:
        print(c, end=' ')
    print(f'Foram informados {len(n)}:\nO maior é o {s}')
maior(1, 10, 20, 4, 6)
maior(3,44,8,56,3,467,322,567,12)
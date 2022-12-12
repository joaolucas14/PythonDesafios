n1= 0
n2= 1
c = 0
x = int(input('Informe quantos elementos de fibonacci: '))
print(n1, n2, end=' ')
while c < (x - 2):
    n3 = n1+ n2
    n1 = n2
    n2 = n3
    c = c+1
    print(n3, end=' ')
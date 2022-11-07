i = int(input("digite o primeiro valor: "))
n = int(input("digite o ultimo valor: "))
x = int(input("digite o valor do incremento: "))
if i < n:
    while i in range(i, n + 1):
        print(i, end = ', ')
        i = i + x
elif i > n:
    while i in range(n, i + 1):
        print(i, end = ', ')
        i = i - x
else:
    print(i)

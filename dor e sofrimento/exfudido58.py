n = int(input("digite o valor de n:\n"))
s = 0
x = 1
i = 1
while x <= n:
    if x % 2 == 0:
        s = s - (1/(i**3))
    else:
        s = s + (1/(i**3))
    x = x + 1
    i = i + 2
s = s * 32
s = s ** (1/3)
print(s)

fib = []
a, b = 0, 1
for i in range(0, 10):
    fib.append(a)
    a, b = b, a + b
    print(fib[i], end = ' ')

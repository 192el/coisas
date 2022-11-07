def fib(n):
    a, b = 0, 1
    for i in range(0,n):
        a,b  = b, a + b
        print(a, end = ', ')
fib(10)

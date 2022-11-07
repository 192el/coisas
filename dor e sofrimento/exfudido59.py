import math
n = int(input("digite um numero:\n"))
euler = []
for i in range(0, n):
    euler.append(1/(math.factorial(i)))
print(sum(euler))

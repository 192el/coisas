from itertools import product
dado = [item for item in range(1, 7)]
num = int(input("digite um numero:\n"))
for i in product(dado, repeat=2):
    if sum(i) == num:
        print(i)

from itertools import product
num = int(input("digite um numero entre 500 e 1000:\n"))
numeros = []
primos = []
x = 0
for i in range (2, num + 1):
    numeros.append(i)
while len(numeros) != 0:
    primos.append(min(numeros))
    temp = [item for item in numeros if item % min(numeros) != 0]
    numeros.clear()
    numeros = [item for item in temp]
    temp.clear()
print("os numeros primos que se somados dão o seu numero são:")
for i in product(primos, repeat=2):
    if sum(i) == num:
        print(i)

import random
lista = []
for i in range(0, 10):
    lista.append(random.randint(0,10))
num = int(input("digite um numero:\n"))
if num in lista:
    print(lista.index(num))
else:
    print("-1")

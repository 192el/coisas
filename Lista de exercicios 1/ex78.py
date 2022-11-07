import random
lista = []
dez = []
for i in range(0, 15):
    a = random.randint(0,1000)
    lista.append(a)
    if a % 10 == 0:
        dez.append(lista.index(a))
print("os numeros multiplos de 10 estão nas posições: ")
for i in range(0, len(dez)):
    print(dez[i])
print(lista)
import random
lista = []
dois = []
for i in range(0, 10):
    a = random.randint(0,1000)
    lista.append(a)
    if a % 2 == 0:
        dois.append(lista.index(a))
print("os numeros multiplos de 2 estão nas posições: ")
for i in range(0, len(dois)):
    print(dois[i])
print(lista)

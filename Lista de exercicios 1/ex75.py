a, b = 1, 1
lista = []
for i in range (0,16):
    lista.append(a)
    a, b = b, a+b
print(lista)
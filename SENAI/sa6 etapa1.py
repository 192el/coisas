def bubbleSort(lista):
    for i in range(len(lista)):
        houveTroca = False
        for y in range(len(lista) - i -1):
            if lista[y] > lista[y + 1]:
                lista[y], lista [y + 1] = lista[y + 1], lista[y]
                houveTroca = True
                if houveTroca == False:
                    break

lista = []
for i in range(10000):
    lista.append(i)
lista.reverse()
bubbleSort(lista)

print(lista)
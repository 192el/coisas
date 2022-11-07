lista = []
par = []
impar = []
for i in range(0, 6):
    num = int(input("digite um numero: "))
    lista.append(num)
print(lista)
y = len(lista)
for i in range(0, y):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    elif lista[i] % 2 != 0:
        impar.append(lista[i])
print(f'você digitou {len(par)} numeros pares e {len(impar)} numeros impares')

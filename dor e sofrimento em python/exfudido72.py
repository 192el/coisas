import random
lista = []
for i in range(0, 10):
    lista.append(random.randint(0,10))
num = int(input("digite um numero:\n"))
if num in lista:
    print(lista.index(num))
else:
    print("-1")
#não é exatamente a mesma coisa que o 71 mas sinceramente o resultado é o mesmo, a diferença é que se fosse escrito em c teria algum desafio, aqui seria só importar mais uma biblioteca, mas o resultado seria o mesmo
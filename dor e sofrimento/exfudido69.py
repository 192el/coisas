import random
a = []
for i in range(0, 15):
    a.append(random.randint(0,10))
num = int(input("digite um numero de 0 a 10:\n"))
b = [item for item in a if item == num]
print(f'esse item aparece {len(b)} vezes na lista gerada aleatoriamente')

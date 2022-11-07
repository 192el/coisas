import random
a = []
for i in range(0, 10):
    a.append(random.randint(0, 999))
b = [item for item in a if item % 2 == 0]
print(f'a quantidade de numeros pares nessa lista aleatoria é de {len(b)}')

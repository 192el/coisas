import random
a = []
for i in range(0, 20):
    a.append(random.randint(0, 999))
print(f'o maior numero nessa lista aleatoria {max(a)} e o menor é {min(a)}')
print(f'suas respectivas posições são {a.index(max(a))} e {a.index(min(a))}')

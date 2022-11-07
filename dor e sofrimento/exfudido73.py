import random
from collections import Counter
lista = []
for i in range(0, 20):
    lista.append(random.randint(0,10))
b = Counter(lista)
print(f"o elemento mais comum é {b.most_common(1)}")
print(f"o elemento central é {lista[10]}")
print(f"a media dessa lista é {sum(lista) / len(lista)}")

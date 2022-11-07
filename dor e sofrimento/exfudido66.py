import random
a = []
for i in range(0, 10):
    a.append(random.randint(0, 999))
b = [item for item in a]
print(b)

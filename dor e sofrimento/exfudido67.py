import random
a = []
b = []
for i in range(0, 10):
    a.append(random.randint(0, 999))
    b.append(random.randint(0, 999))
c = []
c.append(max(a))
c.append(max(b))
print(c)

import random
num = []
ordem = []
for i in range (0,20):
    num.append(random.randint(0,99))
for i in range (0,20):
    ordem.append(min(num))
    num.remove(min(num))
print(ordem)
#e chamam esse de desafio, tenho certeza que já tem um comando que faz isso automaticamente mas eu fui e fiz na unha mesmo
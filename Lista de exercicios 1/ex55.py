import random
from turtle import clear                                                               #é serio esse import random é importante
a = random.randint(1,5)
jogada = int(input("tente adivinhar o numero entre 1 e 5: "))
for i in range(0, 4):
    if jogada != a:
        jogada = int(input(f"você tem mais {4 - i} tentativas: "))
    elif jogada == a:
        print("você acertou!\n")
        print(f"você tinha {i} tentativas sobrando!")
        break

import random
from turtle import clear                                                               #é serio esse import random é importante
a = random.randint(1,5)
jogada = int(input("tente adivinhar o numero entre 1 e 5: "))
if a == jogada:
    print(f'a maquina jogou {a}, você acertou!')
else:
    print(f'a maquina jogou {a}, você errou :(')        #bem mais simples que o outro

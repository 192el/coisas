a = float(input("digite a distancia de um semaforo até o outro em metros:\n"))
b = float(input("digite a velocidade maxima permitida na via em km/h:\n"))
c = float(input("digite a aceleração dos carrosem km/h:\n"))
velocidadeMedia = ((b + c) / 2) / 3.6
distancia = a / 1000
tempo = velocidadeMedia / distancia
print(f"o atraso entre esses semaforos deve ser de {tempo} segundos")

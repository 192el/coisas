largura = float(input("a largura do terreno: "))
comprimento = float(input("digite o comprimento do terreno: "))
area = comprimento * largura
if area <= 100:
    print("esse é um terreno popular")
elif area >= 500:
    print("esse é um terreno VIP")
else:
    print("esse é um terreno master")

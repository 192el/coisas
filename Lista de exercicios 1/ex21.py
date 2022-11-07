ano = int(input("digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("esse ano é bissesto")
elif ano % 100 == 0 and ano % 400 == 0:
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")                                #eu parei pra questionar minha vida enquanto fazia esse
    
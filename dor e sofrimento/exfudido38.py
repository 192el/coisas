ano = int(input("digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("esse ano é bissesto")
elif ano % 100 == 0 and ano % 400 == 0:
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")
#já tava até pronto na outra lista la 
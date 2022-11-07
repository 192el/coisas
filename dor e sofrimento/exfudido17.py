veryCashMoney = int(input("digite o valor que deseja sacar:\n"))
nota100 = []
nota50 = []
nota20 = []
nota10 = []
nota5 = []
nota2 = []
nota1 = []
while veryCashMoney != 0:
    if veryCashMoney - 100 >= 0:
        nota100.append(1)
        veryCashMoney = veryCashMoney - 100
    elif veryCashMoney - 50 >= 0:
        nota50.append(1)
        veryCashMoney = veryCashMoney - 50
    elif veryCashMoney - 20 >= 0:
        nota20.append(1)
        veryCashMoney = veryCashMoney - 20
    elif veryCashMoney - 10 >= 0:
        nota10.append(1)
        veryCashMoney = veryCashMoney - 10
    elif veryCashMoney - 5 >= 0:
        nota5.append(1)
        veryCashMoney = veryCashMoney - 5
    elif veryCashMoney - 2 >= 0:
        nota2.append(1)
        veryCashMoney = veryCashMoney - 2
    elif veryCashMoney - 1 >= 0:
        nota1.append(1)
        veryCashMoney = veryCashMoney - 1
if len(nota100) > 0:
    print(len(nota100), " notas de R$100")
if len(nota50) > 0:
    print(len(nota50), " notas de R$50")
if len(nota20) > 0:
    print(len(nota20), " notas de R$20")
if len(nota10) > 0:
    print(len(nota10), " notas de R$10")
if len(nota5) > 0:
    print(len(nota5), " notas de R$5")
if len(nota2) > 0:
    print(len(nota2), " notas de R$2")
if len(nota1) > 0:
    print(len(nota1), " notas de R$1")

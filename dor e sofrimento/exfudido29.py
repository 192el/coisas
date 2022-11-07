salario = float(input("digite o salario:\n"))
if salario * 0.11 <= 334.29:
    salario = salario - (salario * 0.11)
    print(salario)
else:
    salario = salario - 334.29
    print(salario)

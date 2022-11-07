salarioF = []
salarioM = []
condicao = input("deseja começar? [sim/não]\n")
while condicao == "sim":
    sexo = input("digite o sexo do funcionario [F/M]\n")
    salario = float(input("digite o salario do individuo:\n"))
    if sexo == "F":
        salarioF.append(salario)
    elif sexo == "M":
        salarioM.append(salario)
    condicao = input("deseja continuar? [sim/não]\n")
print(f"o total do salario das mulheres é {sum(salarioF)}")
print(f"o total do salario dos homens é {sum(salarioM)}")

nomes = []
sexos = []
salarios = []
for i in range(0,5):
    sexo = input("digite o sexo do funcionario [F/M]:\n")
    nome = input("digite o nome do funcionario:\n")
    salario = float(input("digite o salario do funcionario: \n"))
    sexos.append(sexo)
    nomes.append(nome)
    salarios.append(salario)
for i in range(0,5):
    if sexos[i] == "F":
        print(nomes[i])
        print(salarios[i])

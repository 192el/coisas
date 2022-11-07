lista = []
idades = []
idadeMulheres = []
idadeHomens = []
for i in range(0, 5):
    sexo = input("digite o sexo da pessoa [F/M]: ")
    lista.append(sexo)
    idade = int(input("digite a idade da pessoa: "))
    idades.append(idade)
    if sexo == "F":
        idadeMulheres.append(idade)
    elif sexo == "M":
        idadeHomens.append(idade)
a = [item for item in lista if item == "M"]
print(f'foram cadastrados {len(a)} homens')
b = [item for item in lista if item == "F"]
print(f'foram cadastrados {len(b)} mulheres')
print(f'a média de idade do grupo é {sum(idades) / len(idades)}')
print(f'A média de idade dos homens é {sum(idadeHomens) / len(idadeHomens)}')
e = [item for item in idadeMulheres if item >= 20]
print(f'tem {len(e)} mulheres com 20 anos ou mais')

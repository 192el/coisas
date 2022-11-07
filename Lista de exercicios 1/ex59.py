idades = []
idadesMulheres = []
homens = []
idadesHomens = []
i = input("deseja começar o programa? [sim/não]\n")
while i == "sim":
    sexo = input("digite o sexo do individuo [F/M]\n")
    idade = int(input("digite a idade do individuo:\n"))
    idades.append(idade)
    if sexo == "F":
        idadesMulheres.append(idade)
    elif sexo == "M":
        idadesHomens.append(idade)
        homens.append(sexo)
    i = input("deseja continuar? [sim/não]\n")
print(f'a maior idade lida é {max(idades)}')
print(f'foram cadastrados {len(homens)} homens')
print(f'a mulher mais nova cadastrada tem {min(idadesMulheres)}')
print(f'a media de idade entre os homens é {sum(idadesHomens) / len(idadesHomens)}')

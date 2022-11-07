nomes = []
nomesMulheres = []
idades = []
idadesMulheres = []
idadesHomens = []
idadeValentina = [69420]
valentina = []
idadeVeio = []
veio = []
i = input("deseja começar o programa? [sim/não]\n")
while i == "sim":
    nome = input("digite o nome:\n")
    nomes.append(nome)
    idade = int(input("digite a idade do individuo:\n"))
    idades.append(idade)
    sexo = input("digite o sexo do individuo [F/M]:\n")
    i = input("deseja continuar o programa? [sim/não]\n")
    if sexo == "F":
        idadesMulheres.append(idade)
        nomesMulheres.append(nome)
    if idade < sum(idadeValentina):
        idadeValentina = [idade]
        valentina = [nome]
    if idade > sum(idadeVeio):
        idadeVeio = [idade]
        veio = [nome]
    if sexo == "M":
        idadesHomens.append(idade)
print(f'a pessoa mais velha tem {idadeVeio} anos e se chama {veio}')
print(f'a mulher mais jovem tem {idadeValentina} anos e se chama {valentina}')
print(f'a media de idade do grupo é {sum(idades) / len(idades)}')
d = [item for item in idadesHomens if item > 30]
print(f'tem {len(d)} homens maiores de 30 anos')
e = [item for item in idadesMulheres if item < 18]
print(f'tem {len(e)} mulheres menores de 18 anos')

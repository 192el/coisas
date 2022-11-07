nomes = []
idades = []
for i in range(0,9):
    nome = input("digite o nome do individuo: \n")
    idade = int(input("digite a idade do individuo: \n"))
    nomes.append(nome) 
    idades.append(idade)
for i in range(0,9):
    if idades[i] < 18:
        print(nomes[i])
        print(idades[i])

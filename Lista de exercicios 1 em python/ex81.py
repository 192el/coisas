idades = []
posicoes =  []
listaVeio = []
veios = []
for i in range(0,8):
    idade = int(input("digite a idade do individuo:\n"))
    idades.append(idade)
    if idade > 25:
        posicoes.append(i)
for i in range(0,8):
    a = max(idades)
    idades[i]
    if idades[i] >= a:
        veios.append(i)
print(f'a media de idade do grupo é {sum(idades) / len(idades)}')
print(f'as pessoas com mais de 25 anos estão nas posições {posicoes}')
print(f'a maior idade digitada foi {max(idades)}')
print(f'a maior idade está presente nas posições {veios}')
adultos = []
idades = []
condicao = input("deseja começar? [sim/não]\n")
while condicao == "sim":
    idade = int(input("digite a idade da pessoa:\n"))
    idades.append(idade)
    condicao = input("deseja continuar? [sim/não]\n")
    if idade > 21:
        adultos.append(idade)
print(f'você digitou {len(idades)} idades')
print(f'a media de idade é {sum(idades) / len(idades)}anos')
print(f'tem {len(adultos)} pessoas com mais de 21 anos')

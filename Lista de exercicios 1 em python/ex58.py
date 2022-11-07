idades = []
idade = 0
while idade != 999:
    idade = int(input("digite a idade do aluno ou digite 999 para finalizar o programa:\n"))
    idades.append(idade)
print(f'a media de idades é {sum(idades) / len(idades)}')

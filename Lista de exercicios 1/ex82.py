notas = []
acima = []
posicoes = []
maximo = []
for i in range (0,10):
    nota = float(input("digite a nota do aluno: \n"))
    notas.append(nota)
for i in range (0,10):
    notas[i]
    if notas[i] > sum(notas) / len(notas):
        acima.append(notas[i])
    if notas[i] == max(notas):
        maximo.append(notas[i])
        posicoes.append(i)
print(f'a média da turma é {sum(notas) / len(notas)}')
print(f'tem {len(acima)} alunos acima da média')
print(f'a maior nota foi {max(notas)}')
print(f'a maior nota foi digitada nas posições {posicoes}')

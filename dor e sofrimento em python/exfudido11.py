notas = []
for i in range(0,4):
    if i < 2:
        nota = int(input(f'digite a {i + 1}° nota do 1° bimestre:\n'))
        notas.append(nota)
    elif i >= 2:
        nota = int(input(f'digite a {i - 1}° nota do 2° bimestre:\n'))
        notas.append(nota)
print(f'a média semestral desse aluno é {sum(notas) / 4}')

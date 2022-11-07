listaIdade = []
for i in range(0, 10):
    idade = int(input("digite a idade de uma das pessoas: "))
    listaIdade.append(idade)
b = [item for item in listaIdade if item >= 18]
c = [item for item in listaIdade if item <= 5]
print(f'a média de idade do grupo é {sum(listaIdade) / len(listaIdade)}')
print(f'as idades das pessoas maiores de 18 são: {b}')
print(f'as idades das pessoas menores de 5 anos são: {c}')
print(f'a pessoa mais velha do grupo tem {max(listaIdade)}')

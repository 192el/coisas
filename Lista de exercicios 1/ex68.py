pesoMulheres = []
pesoHomens = []
for i in range(0,8):
    sexo = input("digite o sexo da pessoa [F/M]:\n")
    peso = float(input("digite o peso dessa pessoa:\n"))
    if sexo == "F":
        pesoMulheres.append(peso)
    elif sexo == "M":
        pesoHomens.append(peso)
print(f'foram cadastradas {len(pesoMulheres)} mulheres')
b = [item for item in pesoHomens if item > 100]
print(f'{len(b)} homens acima de 100kg')
print(f'a media de peso entre as mulheres é {sum(pesoMulheres) / len(pesoMulheres)}')
print(f'o maior peso entre os homens é {max(pesoHomens)}')

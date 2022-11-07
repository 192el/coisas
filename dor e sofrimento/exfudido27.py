numeros = []
ponderado = []
for i in range(0,3):
    num = int(input(f'digite o {i+1}° numero:\n'))
    numeros.append(num)
for i in range(0,3):
    if i == 0 or i == 1:
        ponderado.append(numeros[i] * 2.5)
    elif i == 2:
        ponderado.append(numeros[i] * 5)
print(f'a media ponderada desses numeros é {sum(ponderado) / 3}')
print(ponderado)
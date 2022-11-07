numeros = []
for i in range(0, 5):
    num = float(input(f'digite o {i + 1} numero:\n'))
    numeros.append(num)
print(f'a média é de {sum(numeros) / len(numeros)}')
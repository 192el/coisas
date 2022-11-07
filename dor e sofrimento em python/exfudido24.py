numeros = []
for i in range(0,3):
    num = float(input(f'digite o {i+1}° numero:\n'))
    numeros.append(num)
print(f'o maior numero digitado foi {max(numeros)}')

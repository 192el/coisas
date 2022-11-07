numeros = []
for i in range(0,3):
    num = int(input(f'digite o {i+1}° numero:\n'))
    numeros.append(num)
numeros.remove(min(numeros))
print(f"a soma dos dois maiores numeros dessa lista é: {sum(numeros)}")

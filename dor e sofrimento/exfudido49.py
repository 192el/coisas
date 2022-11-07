num = int(input("digite um numero:\n"))
numeros = []
for i in range (2, num + 1):
    numeros.append(i)
for i in range(0, len(numeros)):
    primos = [item for item in numeros if item % min(numeros) != 0]
    numeros.clear()
    numeros = [item for item in primos]
    primos.clear()
    if numeros == [num]:
        print("é um numero primo")
        break
    elif numeros == []:
        print("não é um numero primo")
        break
    numeros.remove(numeros[0])
    if numeros == [num]:
        print("é um numero primo")
        break
    elif numeros == []:
        print("não é um numero primo")
        break
# o exercicio 48 e o 49 são a mesma coisa isso aqui é mais pra não ficar perdido mesmo
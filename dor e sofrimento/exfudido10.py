numero = int(input("digite um numero menor que 32:\n"))
binario = []
if numero - 16 >= 0:
    binario.append(1)
    numero = numero - 16
else:
    binario.append(0)
if numero - 8 >= 0:
    binario.append(1)
    numero = numero - 8
else:
    binario.append(0)
if numero - 4 >= 0:
    binario.append(1)
    numero = numero - 4
else:
    binario.append(0)
if numero - 2 >= 0:
    binario.append(1)
    numero = numero - 2
else:
    binario.append(0)
if numero - 1 >= 0:
    binario.append(1)
    numero = numero - 1
else:
    binario.append(0)
if numero == 0:
    resultado = ''.join(map(str, binario))
    print(''.join(resultado))
else:
    print("esse numero é 32 ou maior!")

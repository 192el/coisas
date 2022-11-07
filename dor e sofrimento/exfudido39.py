numeroAgencia = list(input("digite o numero da agência:\n"))
numeros = ''.join(numeroAgencia)
agencia = [eval(i) for i in numeroAgencia]
calculo = ((agencia[0] * 5) + (agencia[1] * 4) + (agencia[2] * 3) + (agencia[3] * 2)) % 11
digito = 11 - calculo
print(f'o numero completo da agência é {numeros}-{digito}')

distanciaPercorrida = float(input("digite a distancia percorrida com o carro: "))
diasDeUso = int(input("digite quantos dias o cliente usou o carro: "))
valorCobrado = (90 * diasDeUso) + (0.20 * distanciaPercorrida)
print("o valor a ser cobrado é {}R$".format (valorCobrado))                                         #as mesmas coisas que eu poderia ter feito antes valem aqui
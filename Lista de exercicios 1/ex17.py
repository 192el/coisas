velocidade = float(input("digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("a velocidade está {}km/h acima da velocidade permitida, o valor da mula será de {}".format(velocidade - 80, multa))
else:
    print("a velocidade do carro está dentro do limite permitido")                                          #obedeçam as leis de transito
    

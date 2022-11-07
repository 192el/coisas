segmento1 = float(input("digite o tamanho do primeiro segmento de reta: "))
segmento2 = float(input("digite o tamanho do segundo segmento de reta: "))
segmento3 = float(input("digite o tamanho do terceiro segmento de reta: "))
if segmento1 + segmento2 <= segmento3:
    print("não é possivel formar um triangulo")
elif segmento2 + segmento3 <= segmento1:
    print("não é possivel formar um triangulo")
elif segmento3 + segmento1 <= segmento2:
    print("não é possivel formar um triangulo")
else:
    print("é possivel formar um triangulo")                                         #eu reaproveitei boa parte disso no ex30

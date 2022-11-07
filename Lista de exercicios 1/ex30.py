segmento1 = float(input("digite o tamanho do primeiro segmento de reta: "))
segmento2 = float(input("digite o tamanho do segundo segmento de reta: "))
segmento3 = float(input("digite o tamanho do terceiro segmento de reta: "))
if segmento1 + segmento2 <= segmento3:
    print("não é possivel formar um triangulo")
elif segmento2 + segmento3 <= segmento1:
    print("não é possivel formar um triangulo")
elif segmento3 + segmento1 <= segmento2:
    print("não é possivel formar um triangulo")
elif segmento1 == segmento2 == segmento3:
    print("é um triangulo equilatero")
elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
    print("é um triangulo isóceles")
elif segmento1 != segmento2 and segmento1 != segmento3 and segmento3 != segmento2:
    print("é um triangulo escaleno")

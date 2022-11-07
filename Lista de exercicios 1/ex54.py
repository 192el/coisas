pesos = []
alturas = []
pesosPesados = []
meioQuilos = []
gigantes = []
for i in range (0, 7):
    peso = float(input("digite o peso de uma das pessoas (utilize pontos ex: 70.5): "))
    pesos.append(peso)
    altura = float(input("digite a altura de uma das pessoas (utilize ponto ex (1.70): "))
    alturas.append(altura)
    if peso > 90:
        pesosPesados.append(peso)
    if peso < 50 and altura < 1.60:
        meioQuilos.append(peso)
    if peso > 100 and altura > 1.90:
        gigantes.append(peso)
print(f"a média de altura do grupo é {sum(alturas) / len(alturas)}")
print(f"a quantidade de pessoas acima de 90Kg é {len(pesosPesados)}")
print(f"a quantidade de pessoas que pesam menos de 50Kg e medem menos 1.60m é {len(meioQuilos)}")
print(f"a quantidade de pessoas que medem mais que 1.90m e pesam mais de 100kg é {len(gigantes)}")

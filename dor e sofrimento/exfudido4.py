triangulo = []
for i in range(0,3):
    lado = float(input(f"digite o valor do {i + 1}° lado do triangulo: \n"))
    triangulo.append(lado)
print(f"o perimetro desse triangulo é {sum(triangulo)}")

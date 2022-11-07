x = float(input("digite o valor de x: \n"))
y = float(input("digite o valor de y: \n"))
if x == 0 and y == 0:
    print("o ponto está na origem")
elif x > 0 and y > 0:
    print("o ponto está no primeiro quadrante")
elif x < 0 and y > 0:
    print("o ponto está no segundo quadrante")
elif x < 0 and y < 0:
    print("o ponto está no terceiro quadrante")
elif x > 0 and y < 0:
    print("o ponto está no quarto quadrante")
elif x == 0 and y != 0:
    print("o ponto está em cima do eixo x")
elif x != 0 and y == 0:
    print("o ponto está em cima do eixo y")

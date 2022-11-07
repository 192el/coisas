sombraPredio = float(input("digite o comprimento da sombra do prédio:\n"))
sombraPessoa = float(input("digite o comprimento da sua sombra:\n"))
altura = float(input("digite a sua altura:\n"))
predio = (sombraPredio * altura) / sombraPessoa
print(f'a altura do predio é {predio}')
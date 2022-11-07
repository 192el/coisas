valor = float(input("digite o valor do produto:\n"))
entrada = float(input("digite o valor da entrada:\n"))
if entrada >= valor / 3:
    parcela = (valor - entrada) / 2
    print(f'o valor das duas parcelas será de {parcela}')
else:
    print("o valor da entrada deve ser maior ou igual a um terço do valor total do produto!")

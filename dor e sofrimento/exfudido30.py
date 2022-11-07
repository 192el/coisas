combustivel = input("alcool ou gasolina? [A/G]:\n")
litros = float(input("quantos litros de combustivel deseja abastecer:\n"))
if combustivel.upper() == "A" and litros <= 25:
    print(f"com o desconto o valor vai ficar {((1.90 - (1.90 * 0.02)) * litros):.2f}")
elif combustivel.upper() == "A" and litros > 25:
    print(f"com o desconto o valor vai ficar {((1.90 - (1.90 * 0.04)) * litros):.2f}")
elif combustivel.upper() == "G" and litros <= 25:
    print(f"com o desconto o valor vai ficar {((2.70 - (2.70 * 0.03)) * litros):.2f}")
elif combustivel.upper() == "G" and litros > 25:
    print(f"com o desconto o valor vai ficar {((2.70 - (2.70 * 0.05)) * litros):.2f}")

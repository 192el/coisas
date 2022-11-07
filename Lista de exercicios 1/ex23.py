nome = input("digite o seu nome: ")
sexo = input("digite seu sexo (F/M): ")
valor = int(input("digite o preço do produto: "))
if sexo == "F":
    print(f'o valor do produto com o desconto vai ficar {valor - (valor * 0.13)}, feliz dia da mulher {nome}')
else:
    print(f'o valor do produto com o desconto vai ficar {valor - (valor * 0.05)}')                                              

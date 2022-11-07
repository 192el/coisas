anoNascimento = int(input("digite a sua idade: "))
anoAtual = 2022
idade = anoAtual - anoNascimento
if idade < 16:
    print("você não pode votar")
else:
    print("você pode votar nas eleições")

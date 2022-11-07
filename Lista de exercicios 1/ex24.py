distancia = float(input("digite a distancia em km que você quer percorrer: "))
if distancia < 200:
    print(f'o valor da passagem vai ficar {distancia * 0.50}R$')
else:
    print(f'o valor da passagem vai ficar {(distancia * 0.45):,.2f} R$')            #:,.2f ataca novamente

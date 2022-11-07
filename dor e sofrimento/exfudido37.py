tipoPraga = int(input("digite o tipo de praga: ervas daninhas [1], gafanhotos [2], broca [3], todos acima [4]\n"))
area = float(input("digite a area em acres:\n"))
if tipoPraga == 1:
    custo = area * 50
elif tipoPraga == 2:
    custo = area * 100
elif tipoPraga == 3:
    custo = area * 150
elif tipoPraga == 4:
    custo = area * 250
if area >= 1000:
    custo = custo - (custo * 0.05)
if custo >= 750:
    custo = custo - 750
    custo = custo - (custo * 0.10) + 750
print(f'o valor final ficou de {custo}')

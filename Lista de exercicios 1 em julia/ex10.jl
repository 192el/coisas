print("digite a altura da parede:\n")
altura = parse(Float64, readline())
print("digite a largura da parede:\n")
largura = parse(Float64, readline())
print("a area dessa parede é $(altura * largura)")
print("\n será necessario $((altura * largura) / 2) litros de tinta")

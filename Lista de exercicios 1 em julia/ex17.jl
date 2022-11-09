print("digite a velocidade do carro:\n")
velocidade = parse(Int64, readline())
if velocidade > 80
    print("o valor da multa será de $((velocidade - 80) * 5)")
else
    print("a velocidade está dentro do limite")
end

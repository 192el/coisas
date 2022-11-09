print("digite o preço do produto:\n")
produto = parse(Float64, readline())
print("o preço promocional desse produto é de $(produto - (produto * 0.05))")
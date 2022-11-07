divisor = int(input("digite o divisor:\n"))
dividendo = int(input("digite o dividendo:\n"))
while divisor - dividendo >= 0:
    divisor = divisor - dividendo
print(f"o resto dessa divisão é {divisor}")

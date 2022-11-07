divisor = int(input("digite o divisor:\n"))
dividendo = int(input("digite o dividendo:\n"))
quociente = 0
while divisor - dividendo >= 0:
    divisor = divisor - dividendo
    quociente = quociente + 1
print(f"o quociente dessa divisão é {quociente}")
r1 = int(input("digite o omh da primeira resistencia:\n"))
r2 = int(input("digite o omh da segunda resistencia:\n"))
r3 = int(input("digite o omh da terceira resistencia:\n"))
print(f"a resistencia desse circuito é {1/((1/r1)+(1/r2)) + r3}")
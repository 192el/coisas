num1 = int(input("digite o primeiro valor da progressão aritimética:\n"))
num2 = int(input("digite o valor a ser incrementado:\n"))
soma = []
for i in range(0,10):
    print(num1, end = ', ')
    soma.append(num1)
    num1 = num1 + num2
print(f"\n a soma desses numeros é: {sum(soma)}")

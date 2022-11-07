num1 = int(input("digite um numero:\n"))
num2 = int(input("digite outro numero:\n"))
divisoresNum1 = []
for i in range(1, num1):
    if num1 % i == 0:
        divisoresNum1.append(i)
if sum(divisoresNum1) == num2:
    print("esses numeros são amigos")
else:
    print("esses numeros não são amigos")

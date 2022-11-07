num1 = int(input("digite um numero:\n"))
divisoresNum1 = []
for i in range(1, num1):
    if num1 % i == 0:
        divisoresNum1.append(i)
if sum(divisoresNum1) == num1:
    print("esse numero é perfeito")
else:
    print("esse numero não é perfeito")

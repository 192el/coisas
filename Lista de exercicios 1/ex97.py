num1 = int(input("digite um valor:\n"))
num2 = int(input("digite outro valor:\n"))
num3 = int(input("digite mais um valor:\n"))
numbers = []
def maior(num1, num2, num3):
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)
    return max(numbers), "esse é o maior entre os 3"
print(maior(num1, num2, num3))

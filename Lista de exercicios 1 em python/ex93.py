num1 = int(input("digite o primeiro valor da sequencia: \n"))
num2 = int(input("digite o ultimo valor da sequencia: \n"))
num3 = int(input("digite o valor do incremento: \n"))
num2 = num2 + 1
def contador(num1, num2, num3):
    print(num1)
    for i in range(num1, num2):
        print(num1, end = ',')
        num1 = num1 + num3
contador(num1, num2, num3)

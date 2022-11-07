num1 = int(input("digite o primeiro valor: \n"))
num2 = int(input("digite o ultimo valor: \n"))
somar = []
def superSomador(num1, num2):
    for i in range(num1, num2 + 1):
        somar.append(i)
    return sum(somar)
print(superSomador(num1, num2))
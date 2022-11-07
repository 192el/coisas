num1 = int(input("digite um valor:\n"))
num2 = int(input("digite outro valor:\n"))
def maior(num1, num2):
    if num1 > num2:
        print(f'{num1} > {num2}')
    elif num1 < num2:
        print(f'{num1} < {num2}')
    elif num1 == num2:
        print(f'{num1} = {num2}')
maior(num1, num2)

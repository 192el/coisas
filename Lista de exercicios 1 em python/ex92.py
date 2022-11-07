num1 = int(input("digite um valor:\n"))
def parimpar(num1):
    if num1 % 2 == 0:
        print(f'{num1} é par')
    elif num1 % 2 != 0:
        print(f'{num1} é impar')
parimpar(num1)

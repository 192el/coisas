a = int(input("digite o primeiro numero da sequencia:\n"))
b = int(input("digite o segundo numero da sequencia:\n"))
n = int(input("quantos numeros da sequencia você quer que seja mostrado:\n"))
def fet (a, b, n):
    for i in range(0, n):
        if a % 2 == 0:
            a, b = b, a - b
        elif a % 2 != 0:
            a, b = b, a - b
        print(a, end= ' ')
    return a
print(fet(a, b, n))
#eu acho que é isso a sequencia de fetuccine
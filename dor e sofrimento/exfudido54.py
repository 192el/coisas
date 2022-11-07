numerosTriangulares = []
num = int(input("digite um numero: \n"))
for i in range(0, num):
    numerosTriangulares.append((i+1) * (i+2) * (i+3))
    if max(numerosTriangulares) > num:
        break
if num in numerosTriangulares:
        print(f"{num} é um numero triangular")
else:
    print(f'{num} não é um numero triangular')

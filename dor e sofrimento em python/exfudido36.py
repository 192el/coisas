lista = []
a = []
for i in range(0,5):
    notas = float(input(f"digite a nota da {i + 1}° prova:\n"))
    lista.append(notas)
    if notas >=70:
        a.append(i)
print(lista)
print(a)
if len(a) == 5:
    print("classificação A")
elif a == [0, 1, 2, 3] or a == [0, 1, 3, 4]:
    print("classificação B")
elif a == [0, 1, 2] or a == [0, 1, 3] or [0, 1, 2]:
    print("classificação C")
else:
    print("reprovado")

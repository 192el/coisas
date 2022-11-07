lista = []
num = int(input("digite o numero que sera somado, digite 1111 para sair: "))
lista.append(num)
while num != 1111:
    num = int(input("digite o numero que sera somado, digite 1111 para sair: "))
    if num != 1111:
        lista.append(num)
        resultado = sum(lista)
        print(f"a soma até agora é {resultado}")
    else:
        print(f"você finalizou a soma ao digitar 1111 o resultado final é {resultado}")

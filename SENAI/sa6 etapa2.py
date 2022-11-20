fila = []
def escolha():
    usuario = int(input("digite 1 para adicionar a fila, 2 para tirar item da fila, 3 para limpar a fila, 4 para listar, 5 para verificar se a fila está vazia 0 para sair:\n"))
    return usuario
usuario = escolha()
while usuario != 0:
    if usuario == 1:
        emfilando = int(input("digite quantos items você quer adicionar a fila:\n"))
        for i in range (emfilando):                                              
            coisas = input("adicionando a fila o seguinte item:\n")
            fila.append(coisas)
        usuario = escolha()
    elif usuario == 2:
        emfilando = int(input("digite quantos items deseja retirar da fila:\n"))
        for i in range (emfilando):
            fila.pop(0)
        usuario = escolha()
    elif usuario == 3:
        fila.clear()
        print("fila está limpa!")
        usuario = escolha()
    elif usuario == 4:
        for i in range(len(fila)):
            print(fila[i], f" - {i+1}° item da fila")
        usuario = escolha()
    elif usuario == 5:
        if fila == []:
            print("a fila está vazia")
        else:
            print("a fila não está vazia")
        usuario = escolha()
    if len(fila) == 25:
        print("a fila está cheia!")
print("fechando programa")
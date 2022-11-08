pilha = []
def escolha():
    usuario = int(input("digite 1 para começar a empilhar, 2 para desempilhar item da pilha, 3 para limpar a pilha, 4 para listar, 5 para verificar se a pilha está vazia 0 para sair:\n"))
    return usuario
usuario = escolha()
while usuario != 0:
    if usuario == 1:
        empilhando = int(input("digite quantos items você quer adicionar a pilha:\n"))
        for i in range (empilhando):                                                #descobri que não é necessario escrever (0, x), se for começar com 0 é só colocar o (x) no caso x = empilhando
            coisas = input("adicionando a pilha o seguinte item:\n")
            pilha.append(coisas)
        usuario = escolha()
    elif usuario == 2:
        desempilhando = int(input("digite quantos items deseja retirar de cima da pilha:\n"))
        for i in range (desempilhando):
            pilha.pop()
        usuario = escolha()
    elif usuario == 3:
        pilha.clear()
        usuario = escolha()
    elif usuario == 4:
        print("topo da pilha")
        x = len(pilha) - 1
        while x >= 0:
            print(pilha[x])
            x = x - 1
        print("começo da pilha")
        usuario = escolha()
    elif usuario == 5:
        if pilha == []:
            print("a pilha está vazia")
        else:
            print("a pilha não está vazia")
        usuario = escolha()
    if len(pilha) == 20:
        print("a pilha está cheia!")

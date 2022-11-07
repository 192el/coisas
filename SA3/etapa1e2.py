a = 0
def menu():
    a = int(input("escolha uma opção [1] para cadastrar novo usuário, [2] para listar usuarios cadastrados, [3] para buscar usuario já cadastrado, [4] para apagar um usuario ou [5] para sair do programa: "))
    return a
usuario = []
idadeUsuario = []
while a != 5:
    a = menu()
    if a == 1:
        n = int(input("quantos usuarios quer cadastrar?: "))
        for i in range (0, n):
            nome = str(input("digite o nome do usuario: "))
            usuario.append(nome)
            idade = int(input("digite a idade do usuario: "))
            idadeUsuario.append(idade)
    elif a == 2:
        while True:
            y = len(usuario)
            for i in range(0, y):
                print (usuario[i])
                print (idadeUsuario[i], end = ' anos\n')
            break
    elif a == 3:
        buscar = input("digite o usuario que deseja buscar: ")
        usuarioBuscado = [item for item in usuario if item == buscar]
        posicao = usuario.index(buscar)
        if usuarioBuscado == []:
            print("nenhum usuario foi encontrado")
        else:
            print("o usuario que buscou foi encontrado")
            print(usuarioBuscado[0])
            print(idadeUsuario[posicao], "anos")
    elif a == 4:
        deletarUsuario = input("digite o usuario que deseja deletar: ")
        posicaoDeletar = usuario.index(deletarUsuario)
        usuario.remove(deletarUsuario)
        idadeUsuario.remove(idadeUsuario[posicaoDeletar])
    else: 
        print("numero invalido")
print("programa finalizado")

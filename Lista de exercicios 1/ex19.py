nome = input("nome do aluno: ")
nota1 = int(input("nota da primeira prova do aluno: "))
nota2 = int(input("nota da segunda prova do aluno: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("o aluno {} teve a media de {} e passou de ano".format(nome, media))
else:
    print("o aluno {} teve a media de {} e ficou de recuperação".format(nome, media))

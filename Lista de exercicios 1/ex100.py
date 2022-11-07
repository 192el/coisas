nota1 = int(input("digite a primeira nota do aluno:\n"))
nota2 = int(input("digite a segunda nota do aluno: \n"))
def media(nota1, nota2):
    mediaAluno = (nota1 + nota2)/ 2
    return mediaAluno
print(media(nota1, nota2))
mediaAluno = media(nota1, nota2)
def situacao(mediaAluno):
    if mediaAluno > 7:
        return "APROVADO"
    elif mediaAluno < 4:
        return "REPROVADO"
    else:
        return "em RECUPERAÇÃO"
print(situacao(mediaAluno))

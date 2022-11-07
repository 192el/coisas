nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print("o aluno está reprovado")
elif media >= 7:
    print ("o aluno está aprovado")
else:
    print("aluno está de recuperação")

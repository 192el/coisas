semana = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"]
dia = int(input("digite o dia da semana:\n"))
if dia >= 1 and dia <= 7:
    print(semana[dia - 1])
else:
    print("como funciona sua a sua semana?")
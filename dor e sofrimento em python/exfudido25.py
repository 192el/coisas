mes = int(input("digite o numero do mês:\n"))
if mes == 2:
    print("fevereiro tem 28 dias ou 29, dependendo se é bissesto ou não")
elif mes % 2 == 0 and mes != 2:
    print("esse mês tem 30 dias")
else:
    print("esse mês tem 31 dias")

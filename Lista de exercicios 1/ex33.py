valorCasa = float(input("digite o valor da casa: "))
Salario = float(input("digite o seu salário: "))
anosParaPagar = int(input("digite em quantos anos você pretende financiar ")) * 12
if valorCasa / anosParaPagar > Salario * 0.30:
    print("emprestimo negado")
else: 
    print("emprestimo aceito")

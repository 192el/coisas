nomeFuncionario = input("digite o nome do funcionario: ")
salarioAtual = float(input("digite o salario do funcionario: "))
anosNaEmpresa = int(input("digite quantos anos o funcionario trabalha nessa empresa: "))
if anosNaEmpresa <= 3:
    print(f'o salario reajustado será de {salarioAtual * 1.03}')
elif anosNaEmpresa >= 10:
    print(f'o salario reajustado será de {salarioAtual * 1.20}')
else:
    print(f'o salario reajustado será de {salarioAtual * 1.125}')

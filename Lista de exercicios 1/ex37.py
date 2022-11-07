salarioAtual = float(input("digite o salario do funcionario: "))
genero = input("digite o genero do funcionario [F/M]: ")
anosDeServico = int(input("digite quantos anos o funcionario trabalha na empresa: "))
if genero == "F" and anosDeServico < 15:
    print(f'o novo salario dessa funcionaria é {(salarioAtual * 1.23):,.2f}')
elif genero == "F" and anosDeServico >= 15 and anosDeServico < 20:
    print(f'o novo salario dessa funcionaria é {(salarioAtual * 1.23):,.2f}')
elif genero == "F" and anosDeServico >= 20:
    print(f'o novo salario dessa funcionaria é {(salarioAtual * 1.23):,.2f}')
elif genero == "M" and anosDeServico < 20:
    print(f'o novo salario desse funcionario é {(salarioAtual * 1.03):,.2f}')
elif genero == "M" and anosDeServico >= 20 and anosDeServico < 30:
    print(f'o novo salario desse funcionario é {(salarioAtual * 1.13):,.2f}')
else:
    print(f'o novo salario desse funcionario é {(salarioAtual * 1.25):,.2f}')   #eu espero que não sejam assim os criterios para receber um aumento

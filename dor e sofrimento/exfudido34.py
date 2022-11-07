emprestimo = float(input("digite o valor do emprestimo:\n"))
salario = float(input("digite o seu salario:\n"))
parcela = int(input("digite em quantas parcelas deseja pagar:\n"))
if emprestimo >= salario * 10 and emprestimo / parcela < salario * 0.30:
    print("emprestimo aprovado!")
    print(f'o valor das parcelas serão {parcela} vezes de R${emprestimo / parcela}')
else:
    print("emprestimo rejeitado!")

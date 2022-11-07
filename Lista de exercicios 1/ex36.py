horasDeAtividade = int(input("digite quantas horas de exercicio você fez esse mês: "))
if horasDeAtividade <= 10:
    print(f'você pontuou {horasDeAtividade * 2}, isso vale {horasDeAtividade * 2 * 5} centavos')
elif horasDeAtividade > 10 and horasDeAtividade <= 20:
    print(f'você pontuou {horasDeAtividade * 5}, isso vale {horasDeAtividade * 5 * 5} centavos')
else:
    print(f'você pontuou {horasDeAtividade * 10}, isso vale {horasDeAtividade * 10 * 5} centavos')              #fazer exercicio ta rendendo um monte viu

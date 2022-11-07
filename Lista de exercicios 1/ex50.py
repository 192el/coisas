import random
numerosSorteados = []
numerosSorteadosAcimaCinco = []
numerosSorteadosDivisiveisPorTres = []
for i in range (0,20):
    sorteio = random.randint(0,10)
    numerosSorteados.append(sorteio)
    if sorteio > 5:
        numerosSorteadosAcimaCinco.append(sorteio)
    if sorteio % 3 == 0 and sorteio != 0:
        numerosSorteadosDivisiveisPorTres.append(sorteio)
print(f'\nos numeros sorteados são: {numerosSorteados}')
print(f'\nos numeros sorteados acima de 5 são:{numerosSorteadosAcimaCinco}')
print(f'\nos numeros sorteados divisiveis por 3 são: {numerosSorteadosDivisiveisPorTres}')

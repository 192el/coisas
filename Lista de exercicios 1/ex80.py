import random
numeros = []
posicoes = []
chave = int(input("digite a chave:\n"))
for i in range(0,30):
    a = random.randint(0,15)
    numeros.append(a)
    chaves = [item for item in numeros if item == chave]
    if a == chave:
        posicoes.append(i)
print(f'a sua chave foi encontrada nas posicões {posicoes}\n')
print(f'a sua chave foi encontrada {len(chaves)} vezes')
print(f'os numeros sorteados são {numeros}')

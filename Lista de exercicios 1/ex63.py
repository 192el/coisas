somar = []
condicao = input("deseja começar? [sim/não]\n")
while condicao == "sim":
    some = float(input("digite um numero:\n"))
    somar.append(some)
    condicao = input("deseja continuar? [sim/não]\n")
pares = [item for item in somar if item % 2 == 0]
print(f'a soma de todos os valores é {sum(somar)}')
print(f'o menor valor digitado é {min(somar)}')
print(f'a media dos valores é {sum(somar) / len(somar)}')
print(f'tem {len(pares)} numeros pares')

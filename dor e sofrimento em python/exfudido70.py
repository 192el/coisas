#esse aqui não faz muito sentido fazer em python pq é um conceito que não está presente em python mas da pra limitar uma lista cortando ela caso ela passe de um certo numero
lista = []
while coisa != "SAI" and len(lista) < 100:
    coisa = input('digite qualquer coisa para encher a lista, digite "SAI" para terminar, a lista está limitada a 100 items')
    lista.append(coisa)
print(lista)

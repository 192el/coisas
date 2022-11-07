listaProdutos = []
for i in range(0, 8):
    produtos = int(input("digite o preço do produto: "))
    listaProdutos.append(produtos)
print(f'o preço maximo nessa lista é {max(listaProdutos)}, \no menor preço da lista é {min(listaProdutos)}')

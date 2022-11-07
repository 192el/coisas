anoNascimento = int(input("digite o ano do seu nascimento: "))
anoAtual = int(input("digite o ano atual: "))
idade = anoAtual - anoNascimento
if idade < 18:
    print(f'falta {18 - idade} anos para você precisar se alistar no exercito')
elif idade == 18:
    print("já é ano de você se alistar carai")                                      #falta 2 anos pra mim ainda (medo)
else:
    print(f'você deveria ter se alistado {idade - 18} anos atrás')

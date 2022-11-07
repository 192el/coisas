vogais = list("aeiou")
consoantes = list("bcdefghjklmnpqrstvwxyz")
num = list("0123456789")
digita = input("digite qualquer caractere:\n")
caractere = digita.lower()
if caractere in vogais:
    print("você digitou uma vogal")
elif caractere in consoantes:
    print("você digitou uma consoantes")
elif caractere in num:
    print("você digitou um numero")
else:
    print("você digitou um simbolo")

passesTentados = int(input("digite quantos passes foram tentados:\n"))
passesSucesso = int(input("digite quantos passes foram bem sucedidos:\n"))
quarterBack = ((passesSucesso / passesTentados) - 0.3) / 0.2
def limite(n):
    if n > 2.375:
        n = 2.375
    elif n < 0:
        n = 0
    return n
quarterBack = limite(quarterBack)
jardasPassadas = int(input("digite quantas jardas foram passadas:\n"))
quarterBack1 = ((jardasPassadas / passesTentados)- 3) / 4
quarterBack1 = limite(quarterBack1)
touchDowns = int(input("digite quantos touchdows foram bem sucedidos:\n"))
quarterBack2 = ((touchDowns / passesTentados) / 0.05)
quarterBack2 = limite(quarterBack2)
passesInterceptados = int(input("digite quantos passes foram interceptados:\n"))
quarterBack3 = ((passesInterceptados / passesTentados)-0.095) / 0.04
quarterBack3 = limite(quarterBack3)
resultado = ((quarterBack + quarterBack1 + quarterBack2 + quarterBack3)*100)/6
print(resultado)
print(quarterBack, quarterBack1, quarterBack2, quarterBack3)

#pq?
#futebol americano é o caralho ninguem gosta dessa merda
#tá aqui porque o nome da pasta é dor e sofrimento
#só americanos, mas todo mundo sabe que "estadunidense" nem é gente
#salve pros meus futuros empregadores americanos
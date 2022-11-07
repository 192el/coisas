pontuacao = []
for i in range(0, 3):
    print("--------------------------------------------------------------------------------------------------------")
    golsNossoTime = int(input(f"digite quantos gols nosso time fez na {i + 1}° partida: "))
    golsTimeAdversario = int(input(f"digite quantos gols o time adversário fez na {i + 1}° partida: "))
    if golsNossoTime > golsTimeAdversario:
        pontuacao.append(3)
    elif golsNossoTime == golsTimeAdversario:
        pontuacao.append(1)
print("--------------------------------------------------------------------------------------------------------")
print(f"a pontuação do nosso time é de {sum(pontuacao)} pontos")

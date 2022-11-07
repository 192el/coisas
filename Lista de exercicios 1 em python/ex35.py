tipoCarro = input("digite o tipo de carro (luxo/popular): ")
kmsRodados = float(input("digite quantos kms foram rodados: "))
diasComCarro = int(input("digite quantos dias você ficou com o carro: ")) 
if tipoCarro == "popular" and kmsRodados <= 100:
    print(f'o valor ficou {(diasComCarro * 90) + (0.20 * kmsRodados)}')
elif tipoCarro == "popular" and kmsRodados > 100:
    print(f'o valor ficou {(diasComCarro * 90) + (0.10 * kmsRodados)}')
elif tipoCarro == "luxo" and kmsRodados <= 200:
    print(f'o valor ficou {(diasComCarro * 150) + (0.30 * kmsRodados)}')
elif tipoCarro == "luxo" and kmsRodados > 200:
    print(f'o valor ficou {(diasComCarro * 90) + (0.25 * kmsRodados)}' )
else:
    print("tente usar numeros inteiros e escreva 'luxo' ou 'popular' sem maiusculos")

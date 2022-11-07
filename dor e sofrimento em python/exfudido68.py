junho = [0]
for i in range(1, 31):
    chuva = float(input(f"digite o indice pluviometrico do dia {i}:\n"))
    junho.append(chuva)
print(f'o dia que chuveu mais foi {junho.index(max(junho))}')
quinzena1 = [item for item in junho if junho.index(item) < 16]
quinzena2 = [item for item in junho if junho.index(item) >= 16]
print(f'a média fluviometrica da primeira quinzena de junho é {sum(quinzena1) / (len(quinzena1) - 1)}')
print(f'a media fluviometrica da segunda quinzena de junho é {sum(quinzena2) / len(quinzena2)}')

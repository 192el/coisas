peso = float(input("digite o seu peso em kg: "))
altura = float(input("digite a sua altura em metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("você tem um bom peso")
elif imc >= 25 and imc < 30:
    print("você está acimado do peso")
elif imc >= 30 and imc < 40:
    print("você está obeso")
else:
    print("você tem obesidade morbida")

num = list(input("digite um numero de 0 a 100:\n"))
num1 = [eval(i) for i in num]
unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',] #aquele 'zero' mais pra eu não ter um derrame mesmo 
dezenas = ['zerenta', 'dez', 'vinte', 'trinta' , 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa',] #o zerenta também (confia)
dezes = ['zero', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove']
#agora pra colocar num por extenso
if len(num) == 1:
    print(f'{unidades[num1[0]]}')
if len(num) == 2 and num1[0] == 1:
    print(f'{dezes[num1[1]]}')
elif len(num) == 2 and num1[1] != 0:
    print(f'{dezenas[num1[0]]} e {unidades[num1[1]]}')
elif len(num) == 2:
    print(f'{dezenas[num1[0]]}')
elif len(num) == 3:
    print(f'cem')
if num1 == [0, 0, 0]:
    print("zerocentos e zerenta e zero")
numero = ''.join(num)                                       #isso aqui ta transformando a lista num em uma string
if eval(numero) > 100:                                      #isso aqui ta transformando aquela string em um numero
    print("o numero tem que ser 100 ou menor!")             #muito louco


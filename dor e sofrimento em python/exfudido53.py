a = 5000000
b = 7000000
anos = 0
while a < b:
    a = a + (a * 0.03)
    b = b + (b * 0.02)
    anos = anos + 1
print(f'para a cidade A passar da população da cidade B, vai demorar {anos} anos')

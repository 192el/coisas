from os import sep


i = 30
while i in range (1,31):
    if i % 4 != 0:
        print(i, end = ', ')
        i = i - 1
    elif i % 4 == 0:
        print(f"[{i}]", end = ', ')
        i = i - 1
print("0, acabou!")
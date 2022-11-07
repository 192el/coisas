def gerador(x, n, i):
    if i == 1:
        print("+-------=======------+")
        for i in range(0,n):
            print(x)
        print("+-------=======------+")
    if i == 2:
        print("~~~~~~~~:::::::~~~~~~~")
        for i in range(0,n):
            print(x)
        print("~~~~~~~~:::::::~~~~~~~")
    if i == 3:
        print("<<<<<<<<------->>>>>>>")
        for i in range(0,n):
            print(x)
        print("<<<<<<<<------->>>>>>>")
gerador("Aprendendo python (portugol my balls)", 4, 3)

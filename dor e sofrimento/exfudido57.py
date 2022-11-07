n = int(input("digite um numero:\n"))
s = []
for i in range(1, n):
    s.append((1/i**i))
print(sum(s))


for _ in range(int(input())):
    n = int(input())
    x = (0.143*n) ** n
    if int(x) == 0:
        print(0)
    elif x - int(x) < 0.5:
        print(int(x))
    else:
        print(int(x)+1)
        
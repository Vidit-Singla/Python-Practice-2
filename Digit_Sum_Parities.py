t = int(input())
def sm(n):
    s = str(n)
    z = 0
    for i in s:
        z += int(i)
    return z
for _ in range(t):
    m = int(input())
    x1 = sm(m)
    if x1 % 2 == 0:
        if sm(m+1) % 2 != 0:
            print(m+1)
        else:
            print(m+2)

    
    elif x1 %2 != 0:
        if sm(m+1) % 2 == 0:
            print(m+1)
        else:
            print(m+2)

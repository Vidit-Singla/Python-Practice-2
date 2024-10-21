t = int(input())
for _ in range(t):
    r,s = map(int,input().split())

    if s==1:
        h = 1
    elif s%2 == 0:
        h = s/2
    else:
        h = s//2 + 1

    if r == 1:
        v = 1
    else:
        if r%2 == 0:
            v = r/2
        else:
            v = r//2 + 1
    print(int(v*h))
    




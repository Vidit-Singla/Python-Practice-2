t = int(input())
x = []

for j in range(t):
    d = 0
    l = list(map(int,input().split()))
    n = l[0]
    a = l[1]
    b = l[2]
    for i in range(1,n+1):
        if i%2 == 0:
            d += a
        else:
            d += b
    x.append(d)

for i in x:
    print(i)
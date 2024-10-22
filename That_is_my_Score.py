t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    l = []
    for i in range(n):
        a,b = map(int,input().split())
        if a <= 8:
            l.append([a,b])
            d[a] = 0
    for i in l:
        if d[i[0]] < i[1]:
            d[i[0]] = i[1]
    s = 0
    for i in d:
        s += d[i]
    print(s)
    



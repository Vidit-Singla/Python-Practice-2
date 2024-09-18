t = int(input())
f = []
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    s = 0
    c = 1
    b = True
    for j in l:
        s += j
        if s >= k:
            s -= k
            c += 1
        else:
            f.append('NO '+str(c))
            b = False
            break
    if b == True:        
        f.append('YES')
for k in f:
    print(k)



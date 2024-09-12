def kt(a,b,k):
    x = [0,a,b]
    for i in range(3,k):
        n = x[i-1]+x[i-2]-x[i-3]
        x.append(n)
    return x[k-1]
f = []
t = int(input())
for i in range(t):
    a,b,k = map(int,input().split())
    f.append(kt(a,b,k))
for j in f:
    print(j)
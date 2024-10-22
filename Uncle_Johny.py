t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    k = int(input())
    j = l[k-1]
    l.sort()
    print(l.index(j)+1)

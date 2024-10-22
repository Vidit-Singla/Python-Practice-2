t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    s = 0
    for i in l:
        if abs(i-m) > abs(i-1):
            s += abs(i-m)
        else:
            s += abs(i-1)

    print(s)
for _ in range(int(input())):
    n = int(input())
    g = list(map(int,input().split()))
    f = list(map(int,input().split()))
    s = [(20*g[i] - 10*f[i]) for i in range(n)]
    # for i in range(n):
    if max(s) > 0:
        print(max(s))
    else:
        print(0)
    
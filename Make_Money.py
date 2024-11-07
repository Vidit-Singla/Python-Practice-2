for _ in range(int(input())):
    n,x,c = map(int,input().split())
    l = list(map(int,input().split()))
    f = []
    f.append(sum(l))
    l.sort()
    for i in range(len(l)):
        l[i] = x
        f.append(sum(l)-(c*(i+1)))
    print(max(f))   
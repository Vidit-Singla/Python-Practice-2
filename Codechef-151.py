t = int(input())
f = []
for i in range(t):
    l = list(map(int,input().split()))
    a = l[0]
    b = l[1]
    k = l[2]
    s = [0,a,b]
    d = a-b
    for i in range(k-1):
        if i%2 == 0:
            s.append(s[-1]+a)
        else:
            s.append(s[-1]-d)
    print(s)
    sr = sorted(s)
    print(sr)
    f.append(sr[k-1])
for i in f:
    print(i)


t = int(input())
f = []
for __ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in l:
        d[l.count(i)] = i
    k = d.keys()
    m = max(k)
    f.append(len(l)-m)

for __ in f:
    print(__)

    

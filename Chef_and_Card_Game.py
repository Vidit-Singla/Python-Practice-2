def summer(s):
    l = list(s)
    sm = 0
    for i in l:
        sm += int(i)
    return sm

for _ in range(int(input())):
    n = int(input())
    c = []
    m = []
    s1 = 0
    s2 = 0
    for i in range(n):
        a,b = map(str,input().split())
        c.append(a)
        m.append(b)
    for i in range(n):
        if summer(c[i]>summer(m[i])):
            s1 += 1
        elif summer(c[i]<summer(m[i])):
            s2 += 1
        else:
            s1,s2 += 1
    if s1 > s2:
        print(0)
    elif s2 > s1:
        print(1)
    else:
        print(2)


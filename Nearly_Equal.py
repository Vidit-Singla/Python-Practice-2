t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    a = input()
    b = input()
    a1 = len(a)
    b1 = len(b)
    b2 = b1
    x = []
    for i in range(a1 - b1 + 1):
        x.append(a[i:b2])
        b2 += 1
    c = b1
    l2 = []
    for j in x:
        c1 = 0
        for k in range(b1):
            if j[k] != b[k]:
                c1 += 1
        l2.append(c1)
    print(min(l2))

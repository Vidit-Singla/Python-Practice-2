t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = list(set(l))
    c = 0
    for i in s:
        if l.count(i) % i != 0:
            c += 1
    if c != 0:
        print('NO')
    else:
        print('YES')

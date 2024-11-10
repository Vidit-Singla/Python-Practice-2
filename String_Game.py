for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    f = True
    if n % 2 != 0:
        print('NO')
    elif n % 2 == 0:
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in list(d.values()):
            if i % 2 != 0:
                f = False
        if f:
            print('YES')
        else:
            print('NO')
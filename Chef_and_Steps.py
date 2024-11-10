for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    s = ''
    for i in l:
        if i % k == 0:
            s += '1'
        else:
            s += '0'
    print(s)
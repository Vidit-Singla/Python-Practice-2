for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if n % 2 != 0:
        print('NO')
    else:
        d ={}
        f = True
        s = 0
        l1 = set(l)
        for i in l1:
            d[i] = l.count(i)
        for i in d.values():
            if i % 2 != 0:
                
                f = False
                break
            else:                
                s += i
        if s % 2 == 0 and s != 0:
            print('YES')
        elif f == False:
            print('NO')
            
        

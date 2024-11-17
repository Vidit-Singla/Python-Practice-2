for _ in range(int(input())):
    n,b,m = map(int,input().split())
    t = 0
    while n != 0:
        if n %2 != 0:
            t += (n+1)//2 * m + b
            n -= (n+1)//2
            
            
        else:
            t += (n)//2 * m + b
            n -= (n)//2
           
        
        m *= 2
    print(int(t-b))
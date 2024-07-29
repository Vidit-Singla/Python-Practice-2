try:
    t=int(input())
    for i in range(t):
        n,a=map(int,input().split())
        r=int(n**(0.5))
        p=a*r 
        print(p)
except:
    print(0)
            
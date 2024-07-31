def trib(n):
    a,b,c=0,1,1
    for __ in range(n):
        a,b,c=b,c,a+b+c
        print(a)

n=int(input("range"))
trib(n)
    
 




def persistence(n):
    c=1
    while len(n)<10:  
        for i in n:
            f=1
            n=n*int(i)
            c+=1
    print(c)
persistence('999')

        

def rect(a,b):
    ar = a*b
    m = max(a,b)
    l=[]
    while m!=0:
        while m**2<=ar:
            ar-= m**2
            l.append(m)
        m-=1
    print(l)   
rect(5,3)



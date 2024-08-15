def mptable(n):
    l=[]
    for i in range(1,n+1):
        r= []
        for j in range(1,n+1):
            r.append(i*j)
        l.append(r)
    print(l)

mptable(3)





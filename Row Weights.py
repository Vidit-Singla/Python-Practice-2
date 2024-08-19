def rowweight(l):
    t1= 0
    t2= 0
    for i in l:
        if l.index(i)%2==0:
            t1+=i
        else:
            t2+=i

    print(t1, t2 , sep= ',')

rowweight(([13, 27, 49]))
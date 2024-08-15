def middle(l):
    m= l.index(max(l))
    n= l.index(min(l))
    l1=[0,1,2]
    l1.remove(m)
    l1.remove(n)
    print(l1[0])
middle([5,7,6])


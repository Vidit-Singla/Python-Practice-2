def findeq(l):
    l1= set(l)
    for i in l1:
        if l.count(i)==1:           
            print(i)

findeq([ 1, 1, 1, 2, 1, 1 ])



def sp(l):
    s = 0
    while len(l)>0:
        x = l.pop(0)
        s+=x
        print(l)
    print(s)
sp([0, 1, 3, 6, 10])
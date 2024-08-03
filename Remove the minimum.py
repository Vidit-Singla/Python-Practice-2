def rem_small(l):
    s=min(l)
    while s in l:
        l.remove(s)
    print(l)

rem_small([1,2,3,4,5,1,2,3,4,5])


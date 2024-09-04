def array_diff(l,l1):
    x = l1[0]
    while x in l:
        l.remove(x)
    print(l)
array_diff([1,2,2,2,3],[2])


def asc_ord(t):
    l = list(t)
    lc = l.copy() 
    l1 = []
    while len(lc)!=0:
        m = min(lc)
        l1.append(m)
        lc.remove(m)
    if l == l1:
        return True
    else:
        return False

print(asc_ord((1,2,3,4,5,7,6)))


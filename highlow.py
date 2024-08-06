def highlow(l):
    l1= []
    for i in l:
        l1.append(int(i))
    mi= min(l1)
    ma= max(l1)
    return(str(ma),'and',str(mi))

l= list(map(str, input().split()))
print(highlow(l))
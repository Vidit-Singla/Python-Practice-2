def equal(l):
    for i in range(len(l)):
        if sum(l[:i])==sum(l[i+1:]):
            print(i+1)

equal([1,2,3,4,3,2,1])

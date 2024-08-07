def series(n):
    s=0
    d=1
    for i in range(1,n):
        s+=1/(d+3)
    print(s+1)

series(2)

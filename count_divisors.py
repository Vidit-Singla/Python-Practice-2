def divisor(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
        else:
            continue
    print(l)
divisor(12)

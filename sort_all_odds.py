def sortodd(l):
    l1= []
    for i in l:
        if i%2!=0:
            l1.append(i)
    l1.sort()
    k=0
    for j in range(len(l)):
        if l[j]%2==0:
            continue
        elif l[j]%2!=0:
            l[j]=l1[k]
            k+=1

    print(l)

sortodd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


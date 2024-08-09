def high(l):
    hscore = 0
    for j in l[0]:
        hscore+=ord(j)

    hword = l[0]
    r=0
    for i in l:
        for k in i:
            r+=ord(k)
        if r>hscore:
            hscore=r
        
            hword = i
    print(hword, hscore-(96*len(hword)))

high(['abad'])
    


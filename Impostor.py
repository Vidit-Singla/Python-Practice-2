def findodd(l):
    co= 0
    ce= 0
    for i in l:
        if i%2==0:
            ce+=1
        else:
            co+=1
    if ce>co:
        for j in l:
            if j%2!=0:
                print(j)
            else:
                continue
    elif co>ce:
        for h in l:
            if h%2==0:
                print(h)
            else:
                continue

    else:
        print("No Impostors")

l= list(map(int,input().split()))
findodd(l)
for i in range(int(input("How many test cases: "))):
    n=int(input("How many people: "))
    x= list(map(int,input().split()))
    s= list(set(x))
    dic= {}
    for j in s:
        dic[j]=x.count(j)
    
    m= max(dic.values())
    if list(dic.values()).count(m)>1:
        print("CONFUSED")
    else:
        for k in dic:
            if dic[k]==m:
                print("Laptop",k)
                break


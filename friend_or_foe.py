def filter(l):
    l1=[]
    for i in l:
        if len(i)==4:
            l1.append(i)
    print(l1)
filter({"Ryan", "Kieran", "Jason", "Yous"})

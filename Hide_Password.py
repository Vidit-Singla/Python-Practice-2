def hide_pass():
    s= input("Enter Password: ")
    if len(s)<=4:
        print(s)
    elif len(s)>4:
        l= list(s)
        l1=[]
        l2=[]
        for i in range(-1,-5,-1):
            l1.append(l[i])
            l1.sort()   
        for j in l:
            if j not in l1:
                l2.append("*")
        l=l2+l1
        m=str()
        for i in l:
            m+=i
        print(m)

hide_pass()

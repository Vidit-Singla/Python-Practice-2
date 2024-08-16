def Deadfish(s):
    x = 0
    l=[]
    for i in s:
        if i=='i':
            x+=1
        elif i=='d':
            x-=1
        elif i=='s':
            x = x**2
        elif i=='o':
            l.append(x)
    print(l)
Deadfish('iiisdoso')




def fight(s):
    t1= 0
    t2= 0
    d1 = { 'w':4, 'p':3, 'b':2, 's':1}
    d2 = {'m':4, 'q':3, 'd':2, 'z':1}
    for i in s:
        if i in d1:
            t1+= d1[i]
        elif i in d2:
            t2+= d2[i]
        else:
            pass
    
    if t1 > t2:
        print('Left Side Wins')
    elif t2 > t1:
        print('Right Side Wins')
    else:
        print('Lets fight again')

fight("wwwwwwz")




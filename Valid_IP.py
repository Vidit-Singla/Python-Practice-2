def isip(s):
    l = s.split('.')
    c1 = False
    if len(l)==4:
        c1 = True
    c2 = True
    for i in l:
        if int(i)>255:
            c2= False

    if c1==True and c2 ==True:
        print('Valid')
    else:
        print('Invalid')
isip(input())
def like(l):
    if len(l) == 0:
        print('no one likes this')
    elif len(l) == 1:
        print(l[0], 'likes it')
    elif len(l) == 2:
        print(l[0],',',l[1],'like it')
    elif len(l) == 3:
        print(l[0],',',l[1],'and',l[2],'like it')
    else:
        print(l[0],',',l[1],'and',len(l)-2,'others like this')

like([])
    
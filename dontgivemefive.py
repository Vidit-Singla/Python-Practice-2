def five(a,b):
    c=0
    for i in range(a,b+1):
        if str(i).endswith('5'):
            pass
        else:
            c+=1

    print(c)

five(4,17)
        
def digital_root(n):
    s= str(n)
    c=0
    for i in s:
        c+=int(i)
    print(c)

digital_root(int(input()))

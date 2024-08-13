def tower(n):
    f=1
    for i in range(n):
        print(('*'*f).center(40,' '))
        f+=2


tower(9)

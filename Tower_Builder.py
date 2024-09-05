def tower(n):
    l = []
    for i in range(1,n+1):
        x = ' '*(n-i)
        y = '* '*i
        l.append([x+y])
    for i in l:
        print(i)
        

tower(int(input('How many layers: ')))
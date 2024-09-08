def app(s,x,y,z):
    m1 = min(x,y)
    m2 = max(x,y)
    c = 0
    if z <= s-(x+y):
        c = 0
    elif z <= s-m1:
        c = 1
    else:
        c =2
    print(c)

t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    s = l[0]
    x = l[1]
    y = l[2]
    z = l[3]        
    app(s,x,y,z)





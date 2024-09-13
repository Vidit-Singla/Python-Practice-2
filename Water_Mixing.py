t = int(input())
for i in range(t):
    a,b,x,y = map(int,input().split())
    if b>a:
        if b-a<=x:
            print('YES')
        else:
            print('NO')
    elif a>b:
        if a-b<=y:
            print('YES')
        else:
            print('NO')
    elif a == b:
        print('YES')
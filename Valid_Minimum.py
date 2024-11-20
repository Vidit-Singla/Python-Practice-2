for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a == b == c:
        print('YES')
    elif (a == b and a < c) or (b == c and b < a) or (a == c and a < b):
        print('YES')
    else:
        print('NO')

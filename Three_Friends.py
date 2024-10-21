t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    if x+y == z or y+z == x or x+z == y:
        print('yes')
    else:
        print('no')



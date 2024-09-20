t = int(input())
f = []
for __ in range(t):
    x,y,z= map(int,input().split())
    
    if x>=y:
        f.append('PIZZA')
    elif x>=z:
        f.append('BURGER')
    elif x == y and x == z:
        f.append('PIZZA')
    else:
        f.append('NOTHING')
    
for i in f:
    print(i)
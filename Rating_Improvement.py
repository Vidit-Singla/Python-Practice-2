t = int(input())
l1 = []
for i in range(t):
    l = list(map(int,input().split()))
    x = l[0]
    y = l[1]
    if y>=x and y<=(x+200):
        l1.append('YES')
    else:
        l1.append('NO')

for j in l1:
    print(j,end = ' ')
        
    


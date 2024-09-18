t = int(input())
f = []
for i in range(t):
    l = list(map(int,input().split()))
    d = {1:'A', 2:'B', 3:'C'}
    counter = 0
    for i in l:
        if i>50:
            counter += 1
    if counter == 1:
        x = l.index(max(l))+1
        f.append(d[x])
    else:
        f.append('NOTA')
        
    

for i in f:
    print(i)
    

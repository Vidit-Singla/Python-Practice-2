l = list(map(int,input().split()))
l.sort()
l1= []
for i in range(0,len(l),2):
    c = l[i+1] / l[i]
    l1.append(c)
if len(set(l1)) == 1:
    print('Possible')
else:
    print('Impossible')
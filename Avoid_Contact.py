t = int(input())
f = []
for i in range(t):
    t,c = map(int,input().split())
    n = int(t-c)
    l = []
    for j in range(c):
        l.append('c')
        l.append('_')
    for j in range(n):
        l.append('n')
    if l[-1] == '_':
        l.pop()
    f.append(len(l))

for __ in f:
    print(__)
    

t = int(input())
f = []
for i in range(t):
    a,b = map(int,input().split())
    c = 1
    l = 0 
    bb = 0
    w = []
    while True:
        if c%2 != 0:
            l += c
            if l > a:
                w.append('Bob')
                break
            else:
                c += 1
        elif c %2 == 0:
            bb += c
            if  bb > b:
                w.append('Limak')
                break
            else:
                c += 1
    f.append(w[0])

for j in f:
    print(j)
            

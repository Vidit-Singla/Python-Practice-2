t = int(input())
f = []
for i in range(t):
    m,h = map(int,input().split())
    b = int(m/(h**2))
    if b <= 18:
        f.append(1)
    elif b in range(19,25):
        f.append(2)
    elif b in range(25,30):
        f.append(3)
    else:
        f.append(4)
for j in f:
    print(j)
        

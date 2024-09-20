t = int(input())
f = []
def primechecker(n):
    x = True
    for i in range(2,n):
        if n%i == 0:
            x = False
    return(x)




for __ in range(t):
    n = int(input())
    a = input()
    b = input()
    c = 1
    l = []
    if a == b:
        f.append('YES')
        break
    else:
        for i in range(n):
            if a[i] != b[i]:
                c += 1
            else:
                if c!=0:
                    l.append(c)
                c = 0
    if sum(l) == True:
        f.append('YES')
    else:
        f.append('NO')

for __ in f:
    print(__)



t = int(input())
f = []
for i in range(t):
    dic = {}
    lowers = list(range(ord('a'), ord('z') + 1))
    rev_lowers = list(reversed(lowers))
    for x,y in zip(lowers,rev_lowers):
        dic[chr(x)] = chr(y)


    n = int(input())
    s = input()
    l = list(s)
    for i in range(0,len(s)-1,2):
        l[i], l[i+1] = l[i+1], l[i]
    a= ''.join(l)

    la = list(a)
    for j in range(len(la)):
        la[j] = dic[la[j]]
    b = ''.join(la)
    f.append(b)
    
for j in f:
    print(j)

    

    
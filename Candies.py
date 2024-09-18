t = int(input())
f = []
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = list(set(l))
    

    if len(s) < n:
        f.append('NO')
    else:
      
        for j in s:
            if j in l:
                l.remove(j)
      
        if sorted(l) == sorted(list(set(l))):
            f.append('YES')
        else:
            f.append('NO')

for result in f:
    print(result)

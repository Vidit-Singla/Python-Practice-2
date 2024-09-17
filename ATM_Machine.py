t = int(input())
f1 = []
for cases in range(t):
    p,t = map(int,input().split())
    m = list(map(int,input().split()))
    f = []
    for i in m:
        if i <= t:
            t -= i
            f.append('1')
        else:
            f.append('0')
    f1.append(''.join(f))
    
for j in f1:
    print(j)
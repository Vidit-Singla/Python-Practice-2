t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    l = list(map(int,input().split()))
    for i in range(n-1):
        s += abs(l[i]-l[i+1]) - 1
    print(s)
    

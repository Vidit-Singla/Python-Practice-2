t = int(input())
f = []
for __ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total_sum = sum(a) 
    l1_sum = 0
    found = False

    for i in range(n - 1):
        l1_sum += a[i]  
        l2_sum = total_sum - l1_sum  
        if (l1_sum * l2_sum) % 2 != 0:
            f.append('YES')
            found = True
            break

    if not found:
        f.append('NO')

for result in f:
    print(result)

t =int(input())
f = []
for i in range(t):
    n = int(input())
    s = input()
    c = 0
    for j in s:
        if j not in 'aeiou':
            c += 1
            if c == 4:
                f.append('NO')
                break
        elif j in 'aeiou':
            c = 0
    
    if c<4:
        f.append('YES')

for j in f:
    print(j)




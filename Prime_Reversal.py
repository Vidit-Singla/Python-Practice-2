t = int(input())
f = []

for __ in range(t):
    n = int(input())
    a = input()
    b = input()

    if a.count('1') == b.count('1'):
        f.append('YES')
    else:
        f.append('NO')

for __ in f:
    print(__)

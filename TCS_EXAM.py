t = int(input())
f = []
for __ in range(t):
    d = list(map(int,input().split()))
    s = list(map(int,input().split()))
    if sum(d)>sum(s):
        f.append('DRAGON')
    elif sum(s)>sum(d):
        f.append('SLOTH')
    elif d[0] > s[0]:
        f.append('DRAGON')
    elif s[0] > d[0]:
        f.append('SLOTH')
    elif d[1] > s[1]:
        f.append('DRAGON')
    elif d[1] < s[1]:
        f.append('SLOTH')
    elif d[2] > s[2]:
        f.append('DRAGON')
    elif d[2] < s[2]:
        f.append('SLOTH')
    else:
        f.append('TIE')

for i in f:
    print(i)
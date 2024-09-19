t = int(input())
f = []
for __ in range(t):
    s = input()
    c = 0
    l = []
    for i in s:
        if i == '<':
            l.append('>')
        elif i == '>':
            l.append('<')
        elif i == '*':
            l.append(i)
    for i in range(0,len(l)-2):
        if l[i] == '>' and l[i+1] == '<':
            c+=1
    f.append(c)

for __ in f:
    print(__)
    
    
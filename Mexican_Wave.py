def wave(s):
    l=[]
    for i in range(len(s)):
        l.append(s[:i]+s[i].upper()+s[i+1:])

    print(l)

wave('hello')


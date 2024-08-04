def spliteven(s):
    if len(s)%2!=0:
        s+='_'
    s=list(s)
    l=[]
    while len(s)!=0:
        l.append(s[0:2])
        del s[0:2]
        
    print(l)
spliteven("abcde")

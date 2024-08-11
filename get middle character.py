def getmiddle(s):
    l= len(s)
    l2=int(l/2)
    if l==1:
        print(s)
    elif l%2==0:
        print(s[l2-1:l2+1])
    else:
        print(s[l2])

getmiddle('abcdef')


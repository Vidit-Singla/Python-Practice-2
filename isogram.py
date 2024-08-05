def isogram(s):
    d={}
    c=0
    for i in s:
        d[i]=s.count(i)
    for j in d.values():
        if j>1:
            c+=1
        else:
            continue
    if c==0:
        print("Isogram")
    else:
        print("Not Isogram")

isogram("Dermatoglyphics")
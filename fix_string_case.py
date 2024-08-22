def fixstring(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u+=1
        else:
            l+=1
    if u>l:
        s = s.upper()
    elif l>u:
        s = s.lower()
    else:
        s = s.lower()
    
    print(s)

fixstring(input('String: '))
def weird(s):
    c=''
    for i in range(len(s)):
        if i%2==0:
            c+=s[i].upper()
        elif i%2!=0:
            c+=s[i].lower()
    print(c)
weird('aaaaaaaaaaaaaaaa')
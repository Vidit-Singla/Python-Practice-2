def pin(s):
    c=0
    for i in s:
        if i.isalpha()==True:
            c+=1
        if len(s)!=6:
            c+=1
    if c==0:
        print("Valid")
    else:
        print("Invalid")

pin(input("Enter PIN: "))
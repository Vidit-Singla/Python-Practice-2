while True:
    p= input("Enter password to check validity: ")
    small=False
    big= False
    numb=False
    spc=False
    for i in p:
        if ord(i) in range(97,122):
            small=True
        elif ord(i) in range(65,90):
            big=True
        elif ord(i) in range(97,122):
            small=True
        elif i.isdigit()==True:
            numb=True
        elif i in '$#@':
            spc=True
        else:
            continue
    l=len(p)
    if small==True and big==True and numb==True and spc==True and l in range(6,12):
        print("Valid")
    else:
        print("Invalid")
def issmile(s):
    l= list(s)
    if len(l)==2:
        if l[0] in ';:' and l[1] in ')D':
            print("Valid Smiley")
        else:
            print("Invalid Smiley")
    elif len(l)==3:
        if l[0] in ';:' and l[-1] in ')D' and l[1] in '~-':
            print("Valid Smiley")
        else:
            print("Invalid Smiley")
    else:
        print("Invalid Smiley")

issmile(':(')
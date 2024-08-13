def xo(s):
    co=0
    cx=0
    if 'x' in s or 'o' in s:
        for i in s:
            if i=='o':
                co+=1
            elif i=='x':
                cx+=1
        if co==cx:
            print(True)
        else:
            print(False)

    elif 'x' not in s and 'o' not in s:
        print(True)
xo('hjbbhhhhb')
            

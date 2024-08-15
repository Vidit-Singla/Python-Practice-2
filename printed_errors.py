def perr(s):
    c=0
    for i in s:
        if i not in 'abcdefghijklm':
            c+=1
    print(str(c),'/',str(len(s)),sep='',end='')

perr('aaaxbbbbyyhwawiwjjjwwm')
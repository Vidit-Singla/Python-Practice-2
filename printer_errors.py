def err(s):
    c = 0
    for i in s:
        if i not in 'abcdefghijklm':
            c += 1
    
    print(c,len(s),sep = '/')
    
err(input())


    
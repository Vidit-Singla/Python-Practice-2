def issmile(z):
    c=0
    for j in z:
        l= list(j)
        
        if len(l)==2:
            if l[0] in ';:' and l[1] in ')D':
                
                c+=1
            else:
                continue
                
        elif len(l)==3:
            if l[0] in ';:' and l[-1] in ')D' and l[1] in '~-':
                
                c+=1
            else:
                continue
                
        else:
            continue
            

    print(c)

issmile([':)', ';(', ';}', ':-D'])
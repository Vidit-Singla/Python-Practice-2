def isprop(n):
    s = str(n)
    c=0
    p=1
    for i in s:
        c+=int(i)**p
        p+=1
    if c==n:
        return True
    else:
        return False
    
def check(n):
    l=[]
    for i in range(1,n):
        if isprop(i)==True:
            l.append(i)
    print(l)
check(100)


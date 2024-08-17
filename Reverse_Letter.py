def revi(s):
    l = list(s)  
    l1 = []
    for i in l[::-1]:
        if i.isalpha():  
            l1.append(i)  
    s1 = ''.join(l1)  
    print(s1)  

revi(input(' '))
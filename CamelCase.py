def camelcase(s):
    l = s.split()
    l1=[]
    for i in l:
        l1.append(i.capitalize())
    s1 = ''
    for j in l1:
        s1+=j
    print(s1)

camelcase('camel case test')

    

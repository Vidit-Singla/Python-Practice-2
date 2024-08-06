def roman(s):
    l=list(s)
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    c=0
    for i in l:
        c+= d[i]
    print(c)

roman('MDCLXVI')
def nested(l):
    s = 0
    for i in l:
        m = min(i)
        s+=m
    print(s)

nested([ [ 1, 2, 3, 4, 5 ]      
, [ 5, 6, 7, 8, 9 ]        
, [ 20, 21, 34, 56, 100 ]  
])




        
def arraydif(a,b):
    x= b[0]
    y=[]
    for i in a:
        if i!=x:
            y.append(i)
        
    print(y)
    
arraydif([1,2,2,2,3],[2])
def maxmultiple(div,bound):
    x = 0
    for i in range(bound+1):
        if i % div == 0 and i > x:
            x = i
    
    return x

print(maxmultiple(10,50))

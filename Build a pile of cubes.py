def blocks(m):
    n=1
    vol= 0
    while vol<m:
        vol+=n**3
        if vol==m:
            return n
        n+=1
    
    return -1

print(blocks(int(input("Enter number: "))))


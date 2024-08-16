def dectobin(a,b):
    n=a+b
    b = ''
    while n>0:
        b+= str(n%2)
        n = n//2
    print(b[::-1])

dectobin(10,4)

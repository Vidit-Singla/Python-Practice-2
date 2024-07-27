n=int(input("Range: "))
def gen():
    for i in range(0,n):
        if i%7==0:
            yield i 
        else:
            continue
    
mygen= gen()
while True:
    print(next(mygen))
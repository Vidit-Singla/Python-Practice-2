n= int(input("How many cases: "))
x=0
def mover():
    global x
    m=int(input("How many steps: "))
    if x>0:
        x-=m
    else:
        x+=m
    print(x)
for i in range(n):
    mover()
    
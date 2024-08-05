def divisors(n):
    l=[]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
        else:
            continue
    if len(l)==0:
        print("Number is Prime")
    else:
        print(l)

n= int(input("Enter the number"))
divisors(n)
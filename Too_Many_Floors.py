t= int(input())
l=[]
for i in range(t):
    a,b = map(int,input().split())
    floor = 0
    if a<=b:
        while a!=b:
            if a%10 == 0:
                floor += 1
                a+=1
            else:
                a+=1
    elif a>=b:
        a,b = b,a
        while a!=b:
            if a%10 == 0:
                floor += 1
                a+=1
            else:
                a+=1


    l.append(floor)

for j in l:
    print(j)




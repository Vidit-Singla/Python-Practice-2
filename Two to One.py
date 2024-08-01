n1= input().lower()
n2= input().lower()
a= set((list(n1)))
b= set((list(n2)))
c=[]
for i in a:
    c.append(i)
for j in b:
    if j not in c:
        c.append(j)
    else:
        continue
c.sort()
s=str()
for k in c:
    s+=k
print(s)   

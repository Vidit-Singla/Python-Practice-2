s = input("Enter your string: ")
l= s.split()
l1= set(l)

d=dict()
for i in l:
    d[i]=l.count(i)

print(d)



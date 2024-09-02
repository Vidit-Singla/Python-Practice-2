def fizbuzz(l):
    for i in range(len(l)):
        if l[i]%3 == 0 and l%5 == 0:
            l[i] = 'fizzbuzz'
        elif l[i]%3 == 0:
            l[i] == 'fizz'
        elif l%5 == 0:
            l[i] == 'buzz'

    print(l)

n = int(input())
l = []
for i in range(1,n+1):
    l.append(i)
fizbuzz(l)


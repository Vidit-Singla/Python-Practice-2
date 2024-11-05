def ssort(a,n):
    for i in range(0,n):
        mini = i
        for j in range(i+1,n): 
            if a[j]<a[mini]:
                mini = j
            a[i],a[mini] = a[mini],a[i]
    return a
print(ssort(list(map(int,input("ENTER LIST: ").split())),int(input("ENTER LENGTH OF LIST: "))))
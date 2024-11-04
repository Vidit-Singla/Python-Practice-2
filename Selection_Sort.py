def ssort(a,n):
    for i in range(0,n):
        mini = i
        for j in range(i,n): 
            if a[j]<a[mini]:
                mini = j
            a[i],a[mini] = a[mini],a[i]
    return a
print(ssort([-1 ,-2 ,-5 ,10 ,9 ,8 ,7],7))
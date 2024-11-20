for _ in range(int(input())):
    l = list(map(int,input().split())) 
    d = {}  
    s = input()
    t = 0
    for i in range(len(l)):
        d[chr(i+97)] = l[i]
    for i in d.keys():
        if s.count(i) < 1:
            t += d[i]
    print(t)

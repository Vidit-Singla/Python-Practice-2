def age(l):
    n = 0
    for i in l:
        n+= i*i
    n1 = n**0.5
    print(int(n1/2))

age([65, 60, 75, 55, 60, 63, 64, 45])


def last_digit(n1, n2):
    
    l1 = []
    for i in range(1,5):
        l = (n1**i)%10
        l1.append(l)

    f1 = n2%4
    if f1 == 0:
        print(l1[3])
    else:   
        print(l1[f1-1])

last_digit(2**200, 2**300)
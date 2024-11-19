for _ in range(int(input())):
    s = input()
    c = 0
    for i in s:
        if i.isdigit():
            c += int(i)
    
    print(c)


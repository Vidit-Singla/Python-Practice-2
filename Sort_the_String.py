for _ in range(int(input())):
    s = int(input())
    n = input()
    c = 0
    for i in range(s-1):
        if n[i:i+2] == '10':
            c += 1
    print(c)
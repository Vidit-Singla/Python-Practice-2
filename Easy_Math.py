for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    try:
        l.remove(10)
    except:
        pass
    print(l)
for _ in range(int(input())):
    n = int(input())
    ls1 = input()
    ls2 = input()
    s1 = list(ls1)
    s2 = list(ls2)
    if s1.count(1) == s2.count(1) and s1.count(0) == s2.count(0):
        print('YES')
    else:
        print('NO')
   

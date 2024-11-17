for _ in range(int(input())):
    n = int(input())
    s = input()
    if s.count('0') == s.count('1'):
        print(len(s))
    elif s.count('1') > s.count('0'):
        l = 0
        for i in range(s.count('0')):
            l += 2
        print(l+1)
    elif s.count('0') > s.count('1'):
        l = 0
        for i in range(s.count('1')):
            l += 2
        print(l+1)
    
        
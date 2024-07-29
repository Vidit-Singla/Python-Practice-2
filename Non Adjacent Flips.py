for i in range (int(input())):
    n=int(input())
    s= input()
    if s.count("0")==n:
        print(0)
    else:
        valid=False
        for i in range(n-1):
            if s[i]=="1" and s[i+1]=="1":
                valid=True
                break
        if valid==False:
            print(1)
        else:
            print(2)
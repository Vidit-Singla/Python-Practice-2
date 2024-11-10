for _ in range(int(input())):
    n = int(input())
    fin = list(map(int,input().split()))
    she = list(map(int,input().split()))
    sher = she[::-1]

    f = True
    b = True

    for i in range(n):
        if fin[i] > she[i]:
            f = False
            break

    for i in range(n):
        if fin[i] > sher[i]:
            b = False
            break
    
    if f and b:
        print('both')
    
    elif f:
        print('front')

    elif b:
        print('back')

    else: 
        print('none')
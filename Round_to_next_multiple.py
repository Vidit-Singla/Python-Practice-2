def nextm(n):
    if n % 5 == 0:
        print(n)
    else:
        while n%5 != 0:
            n+=1

        print(n)

nextm(int(input('Enter number: ')))
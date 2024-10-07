import math

def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

c = int(input())
for i in range(c):
    l, h = map(int, input().split())
    for j in range(l, h + 1):
        if prime(j):
            print(j)

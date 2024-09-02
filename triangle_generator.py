def triangle(n):
    for i in range(n,0,-1):
        yield('*'*i)

for x in triangle(3):
    print(x)
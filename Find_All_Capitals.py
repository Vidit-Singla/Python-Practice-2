
def fcap(s):
    l = []
    x = list(s)
    for i,c in enumerate(x):
        if c.isupper():
            l.append(i)
    return l

print(fcap(input()))

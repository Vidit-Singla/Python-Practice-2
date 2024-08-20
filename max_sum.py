def max_sum(l):
    n = max(l)
    l.remove(n)
    n1 = max(l)
    print(n+n1)

max_sum([10, 14, 2, 23, 19])
    
def meeting(s):
    d = {}
    l=[]
    for i in s:
        d[i[0]] = i[1]
        l.append(i[0])
    l = sorted(l)
    print(l)
    l2 = []
    for i in l:
        l2.append((i,d[i]))
    print(tuple(l2))

meeting((('CORWILL', 'FRED'),('CORWILL', 'RAPHAEL'),('CORWILL', 'WILFRED'),('TORNBULL', 'BJON'),('TORNBULL', 'BARNEY'),('CORWILL', 'ALFRED'),('TORNBULL', 'BETTY')))


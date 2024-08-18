def replace(s):
    l = []

    alpha = []
    for i in range(97,123):
        alpha.append(chr(i))
    d = {letter:idx for idx,letter in enumerate(alpha,start=1)}

    l1 = list(s)
    for j in l1:
        if j.lower().isalpha():
            l.append(d[j.lower()])
    
    print(l)

replace("The sunset sets at twelve o' clock.")
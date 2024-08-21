def replace(s):
    c = 0
    alpha = []
    for i in range(97, 123):
        alpha.append(chr(i))
    d = {letter: idx for idx, letter in enumerate(alpha, start=1)}
    
    s = s.replace('a', ' ')
    s = s.replace('e', ' ')
    s = s.replace('i', ' ')
    s = s.replace('o', ' ')
    s = s.replace('u', ' ')
    
    m = 0 
    l = s.split()
    scores = []
    for i in l:
        score = 0
        for j in i:
            score+= d[j]
        scores.append(score)
    print(max(scores))





replace('zzzzzacccccewwwwwwiyyyyyyyofffffufffffff')


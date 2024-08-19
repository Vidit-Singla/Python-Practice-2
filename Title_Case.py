def title_case(a, b):
    b = b.split()
    a = a.split()
    l = []
    for i, word in enumerate(a):
        if i == 0:
            l.append(word.title())
        else:
            if word.lower() in [w.lower() for w in b]:
                l.append(word.lower())
            else:
                l.append(word.title())
    
    x = ' '.join(l)
    print(x)

title_case('THE WIND IN THE WILLOWS', 'The In')

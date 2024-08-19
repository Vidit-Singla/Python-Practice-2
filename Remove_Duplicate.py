def rem(s):
    l=  s.split()
    st= set(l)
    for j in st:
        print(j, sep = ' ', end = ' ')

rem('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')

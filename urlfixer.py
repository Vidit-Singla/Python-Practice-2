def url(s):
    try:
        l= list(s.partition('#'))
        l.remove('#')
        d= ''.join(l)
        print(d)
    except:
        print(s)

url('www.codewars.comabout')
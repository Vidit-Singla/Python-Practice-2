d = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}

def encode(s):
    global d
    for i in s:
        if i in 'aeiou':
            s = s.replace(i,d[i])
    return s
print(encode('bihadi'))

def decode(s1):
    global d
    d1 = {v:k for k,v in d.items()}
    for i in s1:
        if i in '12345':
            s1 = s1.replace(i,d1.get(i))
    return s1
print(decode(encode('bihadi')))


    

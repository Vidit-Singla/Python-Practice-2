def reverse(s):
    l = s.split()
    l1 = []
    for i in l:
        j = i[::-1]
        l1.append(j)
    print(' '.join(l1))
reverse("double  spaces")
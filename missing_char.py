def missing(l):
    for i in range(len(l) - 1):
        if ord(l[i]) != ord(l[i + 1]) - 1:
            print(chr(ord(l[i]) + 1))
            break

missing(['c','d','e','g'])


def disemvowel(s):
    l= list(s)
    for i in l:
        if i in 'aeiou':
            l.remove(i)
    s1=''
    for j in l:
        s1+=j
    print(s1)

disemvowel('abcdefghiou jenfjrnjnfer rgjernrejgnre ekrgnejnge')
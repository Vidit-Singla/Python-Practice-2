def expanded_form(n):
    length= len(n)
    exp= []
    for i in range(length):
        digit= n[i]
        if digit!='0':
            exp.append(digit+"0"*(length-i-1))
        else:
            pass
        
    return '+'.join(exp)
print(expanded_form(input("Enter number: ")))

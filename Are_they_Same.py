def comp(arr1,arr2):
    c=0
    for i in arr1:
        if i**2 in arr2:
            c+=1
                        
        elif i**2 not in arr2:
            print("Not Same")
            break
    if c==len(arr1):
        print("Same")        

x=[1,2,3,4,5,6]
y=[1,4,9,16,25,35]
comp(x,y)


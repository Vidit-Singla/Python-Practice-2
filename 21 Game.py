import random
  
cont=[1,2,3,4]      
nums=[]

com=random.randint(1,4)
for i in range(com):
    nums.append(cont[i])

print("The computer has moved")
print(nums)

while nums[-1]!=21:
    if nums[-1]==20:
        print("Congrats you won!!")
    x=int(input("How many numbers?: "))
    if x>4 or x==0 or x<1:
        print("Please Choose a number b/w 1 and 4")
        break
    else:
        for j in range(x):
            z=int(input("Enter numbers: "))
            if z!=nums[-1]+1:
                print("Incorrect Order")
                continue
            elif z==nums[-1]+1:
                nums.append(z)
    dox=random.randint(1,4)
    for k in range(dox):
        nums.append(nums[-1]+1)
    print("The computer has moved")
    print(nums)
    print("Your Turn")
            




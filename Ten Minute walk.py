import random
dir=['n','s','e','w']
def valid_walk():
    global dir
    l=[]
    corx=0
    cory=0
    for i in range(10):
        x=dir[random.randint(0,3)]
        l.append(x)
        if x=='n':
            cory+=1
        elif x=='s':
            cory-=1
        elif x=='e':
            corx+=1
        elif x=='w':
            corx-=1
    print("Your Coordinates are: ",(corx,cory))
    if corx==0 and cory==0:
        return "Go Ahead"
    else:
        return "Walk will take more than 10 minutes"   

print(valid_walk())

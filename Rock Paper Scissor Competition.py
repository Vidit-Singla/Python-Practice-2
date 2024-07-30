import random
import time

p1 = 0
p2 = 0
choice = ['rock','paper','scissor']

def game():
    global p1,p2,choice
    u = input("Enter your choice: ")
    user_choice = u.lower()
    comp_choice = random.choice(choice)
    print("You said", user_choice)
    print("Computer said", comp_choice)
    if user_choice==comp_choice:
        print("Its a Draw")
        time.sleep(1)
        

    elif ((user_choice=="rock") and (comp_choice=="scissors")):
        print("You win!")
        p1+=1
        time.sleep(1)

    elif ((user_choice=="paper") and (comp_choice=="rock")):
        print("You win!")
        p1+=1
        time.sleep(1)

    elif ((user_choice=="scissors") and (comp_choice=="paper")):
        print("You win!")
        p1+=1
        time.sleep(1)

    else:
        print("You lose!")
        p2+=1
        time.sleep(1)

while p1!=3 or p2!=3 or p1==0 and p2==2 or p1==2 and p2==0:
    game()

if p1==3 or p1==2 and p2==0:
    print("CONGRATS YOU WIN")
else:
    print("YOU LOSE :(")
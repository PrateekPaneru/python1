print('''hello, welcome to the game - rock, paper , scissor
      In this game , we have to choose between one of them
      that is: 1- rock
               2- paper
               3- scissors''')
d="rock"
e="paper"
f= "scissors"


user=input(f"choose one :- {d} , {e} , {f}\n")
import random

print("user choose- " ,  user)
a=random.randint(1,3)
if a== 1:
    print(" comp  choose -" , d)
elif(a==2):
    print("comp choose  - " , e)
elif(a==3):
    print("comp choose  - " , f)

if user==d and a==1:
    print("its a tie")
elif user== e and a==2:
    print("its a tie")
elif user== f and a==3:
    print("its a tie")

if user == d and a==2:
    print("you lose")
elif user== d and a==3:
    print("you win")

if user == e and a==3:
    print("you lose")
elif user== e and a==1:
    print("you win")

if user == f and a==1:
    print("you lose")
elif user== f and a==2:
    print("you win!")
       
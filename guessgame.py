import random
randnumber =random.randint(1,100)
print(randnumber)
user=None
guesses=0
while (user != randnumber):
    user= int(input("enter your guess: "))
    guesses += 1
    if (user==randnumber):
        print("you guessed it right")
       
    else:
        if(user>randnumber):
            print("you guessed the wrong number , enter a smaller number")
        else:
            print("you guessed the wrong number , enter a larger number")
    
    

print(f"your guesses is {guesses}")
with open("hiscore.txt" , "r") as f:
    hiscore=int(f.read())
    if(guesses<hiscore):
        print("you just broke the highscore")
with open("hiscore.txt" , "w") as f:
    f.write(str(guesses))
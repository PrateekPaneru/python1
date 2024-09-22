
import random

c=""
while(True):
        v=random.randint(1,10)
        print(v)
        z=int(input("enter your number"))
        try:
            if c!=0: 
                c=(v/z)
                print(c)        
            if c==1:
                print("remainder is one  ")
                break
            if z==0:
                print("this is an error")
        except ZeroDivisionError as s:
              print(s)          
print("thankyou for coming")
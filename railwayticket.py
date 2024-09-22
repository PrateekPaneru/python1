a=input("enter your name\n")

b=input("Date of birth\n")

c= input("age\n")
d=input("where to where- choose starting position\n")
start= ["kashipur ", "your current location"]
z= input("your final  location\n")
class Railways:
    def Registeration():
        print(f'''name- {a}
DOB-{b}
age-{c}''')
key=None
if (d== "your current location"):
    print(f"your journey is from {start} to {z}" )
if (d=="kashipur"):
    print(f"your journey is from {start} to {z}" )

Railways()
Railways.Registeration()
class Location(Railways):
    k=z
    k= ["moradabad", "bijor", "dehli" , "amroha" , "meerut"]
    while(True):
        if(z!=k):
            break        
        elif z=="moradabad":
            print("the ticket price is - 35")
        elif z=="bijnor":
            print("the ticket price is - 78")
        elif z=="delhi":
            print("the ticket price is - 100")
        elif z=="amroha":
            print("the ticket price is - 56")
        elif z=="meerut":
            print("the ticket price is - 390")
    
input("confirm , Yes/no \n")
x=["paytm" , "googlepay" , "phonepay" , "debit card" , "credit card"]
g=input(f"choose your payment method {x} \n")
m=Location()

def Payment():
    if(g in x):
        print("redirecting to the web page , please wait........")
    

Payment()

n=0
while(n<2):
    n=n+1
    print("thankyou , your ticket is confirmed enjoy your journey")

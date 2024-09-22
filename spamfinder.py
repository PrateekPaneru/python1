a={"spam1":"make a lot of money", 
   "spam2":"buy now " , 
   "spam3":"subscribe this ", 
   "spam4": "click this" ,
   "spam5" : "msignal"}

print("spams are" , a.values())

b=input("enter your text\n")

if("make a lot of money" in b):
    print("your text containing spam-" ,  a["spam1"])
elif("buy now" in b):
    print("your text containing spam-" ,  a["spam2"])
elif("subscribe this" in b):
    print("your text containing spams-" ,  a["spam3"])
elif("click this" in b):
    print("your text containing spams-" ,  a["spam4"])
elif("msignal" in b):
    print("your text containing spams-" ,  a["spam5"])
else:
    print(" your text is free for spam words")





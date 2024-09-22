print("to find the characters in your user name, please write yes")
b=input("type yes- \n")


a=(input("enter the word\n"))

print(len(a))
print("if you want to check whether the username is valid or not ,type yes-\n")
c=input("type yes \n")


if(len(a) > 10):
    print("your usernameis not valid")
elif(len(a) == 10):
    print("your username is not valid")
else:
    print("your username is valid")



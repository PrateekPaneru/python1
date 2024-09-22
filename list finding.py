a=["prateek", "true", "10", "fuck", "real", "bad", "sick"]
if("true" ,"fuck" in a):
    print("list contains errors")
else:
    print("list didnt contains errors")



b=input(" to find the errorous word pls write any digit")
print("true")
print("fuck")

print(input("to clear the error word pls type yes-\n"))
a.remove("true")
a.remove("fuck")
print("the updated list is ", a)
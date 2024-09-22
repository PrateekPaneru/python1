#for loop with range
a= int(input("enter the number"))
print("in this site we solve the digit by getting the square , cube and its table")

b=int(a**2)
c=int(a**3)
d=0
print(f"table of {a} is\n")
for i in range(d,10):
    d=d+1
    print(f"{a} x {d} = {a*d}")
if __name__== "__main__":
    print(f"the square of {a} is {b}") 
    print(f"the cube of {a} is {c}")
 
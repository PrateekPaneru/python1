A= {
"90-100" : "EX",
"80-90" : "A",
"70-80"  : "B",
"60-70"  : "C",
"50-60"  : "D",
}

print(A.items())
b=int(input("type your overall  marks --\n"))

if(b>=90 and b<=100):
    print(A.get("90-100"))
elif(b>=80 and b<=90):
    print("A")
elif(b>=70 and b<=80):
    print("B")
elif(b>=60 and b<=70):
    print("C")
elif(b>=50 and b<=60):
    print("D")
else:
    print("you are failed")
    

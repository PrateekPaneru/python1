a=int(input("enter your marks (english)\n"))
b=int(input("enter your marks (maths)\n"))
c=int(input("enter your marks (hindi)\n"))
#passing_marks_in _each_subject_is_33
paasing_marks= int(33)

if(a>paasing_marks):
    print("congratulations, you are passed in english")
else:
    print("sorry< you are failed in english")

if(b>paasing_marks):
    print("congratulations, you are passed in maths")
else:
    print("sorry< you are failed in maths")

if(c>paasing_marks):
    print("congratulations, you are passed in hindi")

else:
    print("sorry< you are failed in hindi")

e=int(input("enter your total marks outof 300\n"))
total_passing_marks=int(120)

if(e>total_passing_marks):
    print("congratulations, you are passed ")
else:
    print("sorry< you are failed")

percentage =(e/300)*100
print(f"your percentage is {percentage}")
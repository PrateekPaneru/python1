'''we have to make a file called "poem.txt" and save carefully , so only after doing, this thing works'''

with open("poem.txt" ,'w') as f:
    a=f.write("twinkle -twinkle little star , how i wonder what you are")
    a=str(a)
    print(a)
if 'twinkle' in a:
    print("twinkle is present")

f=open("poem.txt")
g= f.read()
if  "twinkle" in g:
    print("twinkle is present")
else:
    print("twinkle is not present")
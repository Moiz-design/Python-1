a=int(input("Enter your age"))
if (a>=18): 
    print(f"Yes You are eligible to get pan card bcoz you are above the required {a} ")
elif(a<=0):
    if(a==0):
        print(f"You have entered {a} which is not valid age so pls add valifd age")
    else:
        print(f"You have entered negative {a} so pls enter valid age")
else:
    print(f"No You are not eligible for pan card ")
# This if elif structure is known as if elif ladder if any one condition is
# satisfied it will discard any other condition

a=int(input("Enter Marks scored in Maths from 100 "))
b=int(input("Enter Marks scored in  Physics 100"))
c=int(input("Enter Marks scored in  Chemistry from 100"))
if a>33 and b>33 and c>33:
    if (a+b+c%3 == 33):
        print("Student was able to pass the 10 std")
else:
    print("Unfortunatly student has failed 10 std")

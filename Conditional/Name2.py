a=[]
for i in range(1,5):
    x=input("Enter A Name")
    a.append(x)
b=input("Enter Name to search ")
for j in a:# This loop works equates each elemnts in a 
    if b != j:
        continue
    else :
        print("Name is in the list")
#  To use original code  with b==j we need to align else with for due to this if we are not able to find any match 
# in for loop it will come out
# else loop can be indented with any loop like for , while, true and etc
# Also if should be there to use else loop ,if does not  follow same indentation rule as else
# We can use same code with == ad it mean present in on

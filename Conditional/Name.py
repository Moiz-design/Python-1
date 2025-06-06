a=[]
for i in range(1,5):
    x=input("Enter A Name")
    a.append(x)
b=input("Enter Name to search ")
k=0
for j in a:
    if b in a:
        k=1       
        break
else:
    print(f"The word {b} is not preseent in list")
# in earlier code b==a here it work like it compare entire list with b due to this it will be neveer true
if k==1:
    print("The given name is in the lists")
# in earlier case we using if b in a print was in for loop due to thsis  it was checking the original condition for each and every element
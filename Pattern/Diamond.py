n=int(input("Enter any no"))
y=n//2
# for upper part of diamond 
for i in range (1,y,2):
    x=n-i
    int(x)
    space=" "*(x//2)
    stars="*"*i
    print(space + stars)
# Lower part of diamond
for i in range(y,0,-2):
    x=n-i
    int(x)
    space=" "*((x//2))
    stars="*"*i
    print(space + stars)
#We can

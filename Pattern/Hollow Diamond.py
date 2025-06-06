n=int(input("Enter any no "))
for i in range (0,n//2,2):
    space=' '*i
    stars="*"*(int(n-i)//2)
    print(stars+space+stars)
for j in range(n//2,-1,-2):
    space=' '*(int(j))
    stars="*"*(int(n-j)//2)
    print(stars+space+stars)
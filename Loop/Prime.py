n=int(input("Enter a no till which u want to print prime no"))
k=0
while n>0:
    for i in range (2,n): # This for loop 
        if n%i==0:  
            k=1
    if n!=1:#To remove "," from last
        if k!=1:
            print(n,end=" * ")
    else :
        print(1)
    n=n-1
    k=0
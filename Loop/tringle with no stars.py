z=set()
n=int(input("Enter no of row"))
for i in range(1,n+1):
    for j in range(1,i):
        a="*"
        b="*"*int(j)
        print(a,end='')
        z.add(len(str(b)))
    k=list(z)
    print(f"({len(k)})")
    print('')#this code prevent stars to be print in single line 

# The abive on print in 1to n 
for i in range(n,1,-1):
    for j in range(i,1,-1):
        print("*",end='')
    print('23')
     # The below one print fromm n 2 1

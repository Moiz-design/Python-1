def great(b,c,d):
    a=[b,c,d]
    n=len(a)
    m=0
    while n>0:
        for i in a :
            if i>m:
                m=i
        n-=1
    return m
b=int(input("Enter a no"))
c=int(input("Enter a no"))
d=int(input("Enter a no"))
n=great(b,c,d)
print(f"The greatest no from {b},{c},{d} is {n}")   
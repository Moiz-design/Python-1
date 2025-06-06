n=int(input("Enter any no"))
j=1
i=0
b=1
a=0
for k in range(0,n-2):
    print(i)
    print(j)
    i+=j
    j+=i
while n>0:
    print(a,b)
    a+=b
    b+=a
    n-=1
    
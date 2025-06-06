# To Devlop python algorithm to calculate summition of even and odd number btw the given 2 number
a=int(input("Enter Two Number :- "))
b=int(input("Enter Two Number :- "))
n=int(input("1= Summition of odd no and 2= Summition of even no :- "))
Even_Sum=0
Odd_Sum=0
if a>=b:
    print(1)
    for i in range (b,a+1):
        if i%2==0:
            Even_Sum+=i
        elif i%2!=0:
            Odd_Sum+=i
elif b>a:
    for i in range (a,b+1):
        if i%2==0:
            Even_Sum+=i
        elif i%2!= 0:
            Odd_Sum+=i
if n==1 :
    print(f"The sum of odd number btw 2 NUmber is {Odd_Sum}")
elif n==1 :
    print(f"The sum of Even number btw 2 NUmber is {Even_Sum}")
print(sum(i for i in range(a,b+1) if i%2 == 0 ))
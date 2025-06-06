def fac(x):
    if x!=0:
        return x*fac(x-1)
    else:
        return(1)
a=int(input("No of objects"))
b=int(input("How many of then to chose at one time "))
if a>b:
    n=fac(a)
    r=fac(b)
    c=fac(a-b)
    m=n/(r*c)
    print(f"No of way to chose {b} from {a} is {m}")
else:
    print(f"Not possible as no of was {a} is greater than actual content{b}")
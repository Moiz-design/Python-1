b=input("Enter any name for which u want to reverse :- ")
c=list(b)
print(c)
d=""
for i in b:
    k=c.pop()
    if len(c)==0:# This is if conditon execute when 
        d+=k.lower()
    elif len(b)-1==len(c):
        d+=k.upper()
    else:
        d+=k
print(d)
    
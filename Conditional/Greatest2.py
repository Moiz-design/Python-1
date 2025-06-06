a=[]
for i in range (1,4):
    x=int(input("Enter any no"))
    a.append(x)
print(a)
c=0
d=0
for b in a:
    if c<b:
        c=b
for b in a:#This give sum of all no
    d += b
print(d)
print(c)
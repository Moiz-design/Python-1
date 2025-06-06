n=int(input("Enter no of "))
a=[]
for i in range(1,n+1):
    k=input(f"Enter a Element you want to add")
    a.append(k)
for i in range(0,len(a)):
    a[i]=a[i][::-1]
    a[i]= a[i].capitalize()
print(a)
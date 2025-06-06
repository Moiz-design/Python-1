n=int(input("Enter the no of data points you have :- "))
Value_y = []
Value_x=[]
for i in range (0,n):
    xi=int(input(f"Enter the value of x{i} :-"))
    Value_x.append(xi)
for i in range (0,n):
    yi=int(input(f"Enter the value of y{i} :-"))
    Value_y.append(yi)
langrage = []
x=int(input("Enter the value of x for which y is required :- "))
for j in range (0,n):
    pr=1
    for i in range(0,n):
        if i!=j:
            pr =  pr* (x-Value_x[i])/(Value_x[j]-Value_x[i])
    langrage.append(pr)

Unkown_value = 0
for i in range (0,n):
    Unkown_value += langrage[i]*Value_y[i]
print(f"The required Value of y at {x} is {Unkown_value}")


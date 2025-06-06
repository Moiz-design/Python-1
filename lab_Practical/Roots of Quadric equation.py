import math as m
def Root(a,b,c):
    Delta=b**2 -   4*a*c
    a= 2*a 
    if Delta <0 :
        raise ValueError("The given equation has imaginary root")# This prevent program to rin if given equation has imaginaru roots
    root_1 = (-b + m.sqrt(Delta))/ a
    root_2= (-b - m.sqrt(Delta) )/a
    print(f"The Root of THe given equation is {root_1} and {root_2}")
a=int(input("Enter The coefficent of x^2 :- "))
b=int(input("Enter The coefficent of x :- "))
c=int(input("Enter The Constant :- "))
Root(a,b,c)

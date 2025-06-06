def fxn(n):
     if n!=0:
         return n*fxn(n-1)
     else :
         return 1
n=int(input("Enter any NO "))
x=fxn(n)
print(x)

"""If u want to continuasly calll a fxn inn fxn u need to write the code for termination firsty otherwise it will go one cause errror
and to use a result of fxn outside it u need to first catch valuse by assigning a varible to cathc the """
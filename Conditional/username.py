a=input("Enter your username")
z=a.count(" ")#This Check Wether given string containg any space or not 
if z>0:
    a.replace(" ","")#This replace Any space in string 
    if len(a)>10: 
        print("Truth")
    else :
        print("False")
elif z==0:
    if len(a)>10:
        print("Truth")
    else:
        print("False")
print(a.replace(" ",'/t'))
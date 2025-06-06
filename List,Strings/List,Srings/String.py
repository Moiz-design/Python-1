c = "Moiz Has scored 98 in  IVSSC"
d = len(c)
k=c.index('o')#This gives first index of letter u are looking for
print(k)
print(d)
print(c.count(""))#  This fxn count no of specific words in string
d=c.replace("  ","1") #Replace fxn replace gthe given word with new word
print(c)
print("12".join(c)) # This inset left string in every letter of other string
a=input("Enter User name")
b=str(a)#This is not required as input is alrezdy converted to string
print("Good Afternoon"+b)
e=input("Enter your Name")
f=int(input("Enter Your date"))
print("leter",''' Dear''' , e,''' You are selected !"''',f)
z=c[1:20:4]#This is same aas slicing lists
print(z)
# \t add tab space btw two letter
#\n add new line
#\\ add bckslask,\' add single quotes 

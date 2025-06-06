import os 
print(os.path.exists("Moiz1.txt"))#os.path.exist("Name") This check wether the given name exist on the given path output true , false
if os.path.exists("Moiz1.txt"):
    os.rename("Moiz1.txt","Moiz.txt")#This will rename the file from original name with new name 
with open("Moiz.txt","r")as f:
    c= f.read()
with open("Moiz_copy.txt","w") as z:
    z.write(c)
#The above Code Copy the content of file and then open and copy to new file 
if os.path.exists("Moiz_copy.txt"):
    os.remove("Moiz_copy.txt") # This remove designated file from computer
if os.path.exists("Moiz_copy.txt") == False:
    print("The file has been  succesfully removed")

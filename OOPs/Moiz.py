import statistics as m
class student :
    #Class Is Blueprint to make car so an object is specific car 
    # Class instances is like Engine and fuels which is being used 
    # Fx 
    standard = 10 # This is class attribute which is defined when single varible is used again and again due to which use this 
    def __init__(self,n):
        self.Marks=[]#After Defining variable as self.name then it became an instance attribute which will be used in all format for all code 
            #for that partiular object whcih is been call
                #o
        for i in range (0,n):
           self.Marks.append(int(input("Enter marks in subject")))
    def Average (self) :
        avg = m.mean(self.Marks)
    
        print(f"The average score of studetn is {avg}")
k=int(input("Enter Total No Student "))
n=int(input("Enter Total No Subjects "))
Student={}
for i in range (0,k):
    Si=student(n)
    n=input("Enter Name")
    Avg=Si.Average()
    Student[n]=Avg
Student.valu
                  

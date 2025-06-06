def New_Task(n):
    no_of_task=int(input("Enter no of Task"))
    for  i in range(1,no_of_task+1):
        Date=n
        Task=input("Enter Your Task")
        New_Deadline=input("Enter Your Task deadline")
        status=input("Completor or Pending ")
        with open(r"C:\Users\moizr\OneDrive\Desktop\Coding\Python\File Open\Daily_Task.txt", "a") as f:
            f.write(str(Date) + "\n")  # Write the date and move to a new line
            f.write(f"Task: {Task}\nDeadline: {New_Deadline}\n")
            f.write(f"status : {status}\n")
from datetime import date
# Get today's date
Today_Date= date.today()
New_Task(Today_Date)
def Updated():
    Updated_task=input("Updated or not ")
    with open(r"C:\Users\moizr\OneDrive\Desktop\Coding\Python\File Open\Daily_Task.txt", "r") as f:
        task=f.readlines()
    print(task)
Updated()
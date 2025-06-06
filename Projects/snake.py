import random as r
def snake():
    a=[1,2,3]
    compute =0
    Human=0
    while compute!=3 and Human!=3:
        print(""" 1 = Snake \n 2 = Water \n 3 = Gun""")
        b=int(input("Enter a Your Choice" ))
        for i in range (1):
            choice=r.choice(a)
        if (choice ==3 and b==1) or (choice ==1 and b==2) or (choice==2 and b==3)  :
            print(f"haha You lost as {choice} beats {b}")
            compute+=1
        elif (choice==3 and b==3) or (choice ==2 and b==2) or (choice==1 and b==1):
            print(f"No one win as your choice {b} is same as mine {choice}")
        elif (choice==3 and b==2) or (choice==1 and b==3) or (choice==2 and b==1):
            print(f"Ahh! You Won As {b} beats{choice}",)
            Human+=1
    else:
        if compute==3:
            print("hahaha I won ")
        else:
            print("Ahh! You win")
# c=input("Enter ur name")
snake()
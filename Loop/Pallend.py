n=int(input("Input any No"))
Original_no=n
i=0
reverse_n=0
while n>0:
    i=n%10 #This is remainder fxn which divide fxn with 10  and gives modulo
    reverse_n = reverse_n*10+i# This equation add last no from previous step and to reverse_no but first it is multiplied by 10
    n = n//10 #This does floor diviso and remove last 2 digits 
# In if we should not use n bcoz as loop ends n chage to 0 
if reverse_n==Original_no:
    print("No is Pallindrome")
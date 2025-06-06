import math as m

# Taking inputs correctly
Th1 = int(input("Enter the temperature of hot fluid while entering: "))
Th2 = int(input("Enter the temperature of hot fluid while exiting: "))
Tc1 = int(input("Enter the temperature of cold fluid while entering: "))
Tc2 = int(input("Enter the temperature of cold fluid while exiting: "))

# Choosing flow type
n = int(input("1: For CoCurrent , 2: For Counter Current: "))

# Calculating temperature differences
if n == 1:
    a = Th1 - Tc1
    b = Th2 - Tc2
elif n == 2:
    a = Th1 - Tc2
    b = Th2 - Tc1
else:
    print("Invalid input for flow type!")
    exit()

# Handling the case where log(a/b) could be undefined
if a == b:
    print("LMTD is undefined (temperature difference is constant).")
else:
    LMTD = (a - b) / m.log(a / b)
    print(f"LMTD: {LMTD:.2f}")

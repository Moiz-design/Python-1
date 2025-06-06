with open("Prob_1.txt","r") as f:
    c=f.read()
k="twinkle"
t=0
for i in c:
    if k.upper or  k in c():
        t=1
if t==1:
    print(f"{k} is present in file ")
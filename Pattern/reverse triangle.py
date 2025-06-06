n=24
y=120
# %%%
for i in range(y,0,-2):
    x=y-i
    int(x)
# %%%
    space=" "*((int(x)//2))
    stars="*"*i
    print(space + stars + space)

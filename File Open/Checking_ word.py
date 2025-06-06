def fxn():
    word="Python"
    n=0
    with open ("Python.txt","r+") as f:
        c=f.readline()
        while c:
            for i in c:
                if c.upper() in i.upper():
                    print(f"The given file contain {word}")
            c=f.readline()
            n+=1
    return n
y=fxn()
print(f"The given file contain {y} no of lines")
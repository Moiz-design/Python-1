for a in range(2,21):
    n=1
    with open("My file","a") as f:
        f.write(f"The multiplication table of {a} is as follows"+"\n")
        while n!=10:
            m=a*n
            f.write(f"{a}*{n} is {m}"+"\n")
            n+=1

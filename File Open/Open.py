f=open("first.txt",'w')
for i in range (1,10):
    print(i)
    f.write(str(i)+'\t')
f.close()
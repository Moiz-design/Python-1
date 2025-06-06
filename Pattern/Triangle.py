n=int(input("Enter a no"))
for i in range (1,n+1,2):
    spaces=' '*(int(n-i)//2)
    stars=""
    st2=""
    for j in range(1,i//2):
        stars+=str(j)
    for j in range(i//2,0,-1):
        st2+=str(j)
    print(spaces+stars+st2)
a="Moiz is good"
print(a+stars+st2)
"""Earlier code where we i use stars =str(j)*i this print ex j=3, i=4(3333) rather 4321
so to get desired one we need to add j as string instead of mutliplying
"""

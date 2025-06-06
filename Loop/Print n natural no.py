n=int(input("Enter the no till you want to "))
x=1
while x<=n:
    print(x)
    if x==n:
        print('\n')
    x+=1
#here if we write if condition after x+=1 it will get execute one step ahead bcoz
#after print x will be equal to n when executing 2nd last step due to this
#it will leave line if n=10 at 9 instead of 10 due to this we
#we make x+=1 run after if clause
while n>0:
    if n==1:
        print(n)
    else:
        print(n,end=' , ')
    n-=1
#end is operator in print fxn which specify what should be added after  that n like "' '" this end space 
#and excute the code in single line
#  for and else is 

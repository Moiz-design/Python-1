a=[] # Lists are mutable , indexed fxn 
for i in range(1,6):
   b=int(input("Enter any No"))
   a.append(b)
a.sort()
print(a)
j=0
for j in range(1,len(a)+1):
   j+=a.pop()
print(j)
# """ Fxn that can be perform on lists:-
# slice:-a[intial index:Final index:Steps to skip] it can be also used to reverse 
# sort:-a.sort()
# insert:-a.insert(object to be added:at which index to be added
# pop:-a.pop() Removes item from last 
# append:- a.append(x) add x at last of lists
# This operation does not changes list it creates a whole new lists with desirable qualities

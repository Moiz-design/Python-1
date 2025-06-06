s=set()
c={"Nepal","Moiz","Zainab"}
b={9,"Moiz","Ayush ",3,}
for i in range(1,4):
  x=input("Enter any no to set")
  s.add(x)

z={x for x in range(len(s))}
print(s,type(s))
print(s.union(b.union(c))) # Just like The regular maths it will print all unique element of desired set
print(s.intersection(b))# It gives all the comman and unique elemntns which is present set
print(s.issubset(c))# it tells if the a is subset of c or not
print(s - c, c-s)  # First reprsent element which is only in s not even comman similar second reprsent elements only in c 
# - is reprsenting diffrence
print(z)
k=list(s)#converte the set to the list
m=set(k)#Again converte list to set 
print(type(k),k,type(m),m)

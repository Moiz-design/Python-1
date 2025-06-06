# c={1,2,[3,2]}n is wrong
#  We can not alter the lists which is present in set although list is mutiable  set is also muitable
# but the elements which is being added should be immutable 
c={2,3,frozenset([3,"Harry"])} # frozen set randered set immutable while creating frozen set we need to use () this instead of{}
s={}
print(type(s))
# <class 'dict'>
a=set()
print(type(a))
# <class 'set'>

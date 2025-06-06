a="Make a lot of money"
b="Buy Now"
c="Subscribe this"
d=" Click this "
e=input("Enter a comment")
if a.upper() in e.upper() or b.upper() in e.upper() or c.upper() in e.upper() or d.upper() in e.upper() :
    print("Comment is spam")
    # in operation checks if the given item is in the specifed objects
    #if(a,b,c,d,in e) is not valid bcoz , creates a new tuples of a,b,c,d so due to this condition just check tuple 
    #itself not an indivisual elements one by one
    
else:
    print("Comment is legit")
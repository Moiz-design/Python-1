p=int(input("Enter A no"))# 5
q=int(input("Enter A no"))#3
p=p^q# This is 5^3
q=p^q#this (5^3)^5
p=p^q # This (5^3)^3
print(f"{p=} and {q=}")
p,q=q,p
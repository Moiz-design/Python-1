
a = {}
c = {"Moiz": "Home", "Zain": "Bully"}
for i in range(1, 3):
    key = input("Enter The Hindi Words: ")
    value = input("Enter The English Translation: ")
    a[key] = value
    a.update(c) #Merges two diffrent dictonary into new one
# Here if we use same key more than one time that it will get replace by the newest value
# ex :- if first we enter key =1 and value = 9 then again key=1 and value=10
# then in dict 9 will be replaced by 10  
# But if values are same but keys are diffrent then for both the key value will be same it will not get replace
for key, value in a.items():
    print(f"Key: {key}, Value: {value}")
# This for works like a.items returns every key,value pair in turple form than first one is assigned asn keys and second one is assigned as vvalue then it is being sent to print
# here f is fxn known as formatted string it is use to put variable in string 

z=a.items()
y=list(z)
print(type(y),y[0:1])
print(a.items(), type(a.items())) # Give all items with key along with their values
print(a.keys())# Give all keys that is present in dictionary
print(a.values())#Give all Values that is present in dictionary
print(type(a),len(a))
b=input("Enter the word for which you want translation ")
if b in a:
    print(a[b])
else :
    print(f"The {b} is not presernt is dictionary")

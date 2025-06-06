a=input("Enter The key word you are looking for")
b=input("Enter The post ")
if a.upper() in b.upper():
    print(f"The enter post {b} contain key {a} that you are looking for ")
else: 
    print(f"The post {b} does not contain name { a} in it")
# ask the user to enter their name and greet them accordingly
name = str(input("enter your name:"))
if name == "Alice":
    print ("Hello Alice")
else:
    print ("Hello stranger")    

# OR.....to make it case-insensitive

name = str(input("enter your name:"))
if name.lower() == "alice":
    print ("Hello Alice")
else:
    print ("Hello stranger")    
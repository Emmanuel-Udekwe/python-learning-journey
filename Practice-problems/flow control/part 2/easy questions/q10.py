# ask the user for two strings and check if they are equal
string1 = str(input("enter first string:"))
string2 = str(input("enter second string:"))
if string1 == string2:
    print ("same string")
else:
    print("different string")    

# OR...........TO make it case-insensitve

# ask the user for two strings and check if they are equal
string1 = str(input("enter first string:"))
string2 = str(input("enter second string:"))
if string1.lower() == string2.lower():
    print ("same string")
else:
    print("different string")    

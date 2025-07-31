# ask for age and categorize as child, teenager or adult
age = int(input("enter your age:"))
if age < 13:
    print ("child")
elif age < 20:
    print ("Teenager")  
else:
    print ("adult")      
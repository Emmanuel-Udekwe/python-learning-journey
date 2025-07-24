# ask the user's age and if they have a drivers license. print if both conditions are true
age = int(input("enter your age:"))
drivers_licence = input("Do you have a driver licence (True/False):") == True
print (age >= 18 and drivers_licence)
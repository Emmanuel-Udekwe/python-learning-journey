# ask for 3 side length and check if they can form a triangle
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
num3 = float(input("enter third number:"))
if ((num1 + num2) > num3) and ((num1 + num3) > num2) and ((num2 + num3) > num1):
    print ("yes")
else:
    print ("no")   
# ask the user for two numbers and compare them.
# print which one is greater or if they are equal
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1 > num2:
    print ("num1 is greater")
elif num2 > num1:
    print("num2 is greater")   
elif num1 == num2:
    print ("numbers are equal")     
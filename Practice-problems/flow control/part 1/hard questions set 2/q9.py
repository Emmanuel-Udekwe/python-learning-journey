# ask for color and two numbers
color = str(input("enter a colour:"))
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
# check the logic
print (color.lower() == "blue") and (not(num1 == num2)) or (num1 + num2 < 10)
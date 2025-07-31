# ask the user for two numbers and an operation (add or subtract)
# perform the selected operation. print an error if its invalid
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operation = str(input("enter an operation (add or subtract):")).lower()
if operation == "add":
    print ("The sum is:",num1 + num2)
elif operation == "subtract":
    print ("The result is:",num1 - num2) 
else:
    print ("invalid operation")    
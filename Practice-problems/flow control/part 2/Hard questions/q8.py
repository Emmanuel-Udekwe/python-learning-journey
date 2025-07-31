# simple calculator: perform basic maths operation based on user input....
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
math_operator = str(input("enter a mathematical operator (+ or - or * or /):"))
if math_operator == "+":
    print (num1 + num2)
elif math_operator == "-":
    print (num1 - num2)
elif math_operator == "*":
    print (num1 * num2)   
elif math_operator == "/":
    print (num1 / num2)   
else:
    print ("invalid operator")    
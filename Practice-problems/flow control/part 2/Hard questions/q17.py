# count how many of three user-centered numbers are positive using a counter
num1 = int(input("enter first integer:"))
num2 = int(input("enter second integer:"))
num3 = int(input("enter third integer:"))

count = 0

if num1 > 10 and num1 % 2 == 0:
    count += 1
elif num2 > 10 and num2 % 2 == 0:
    count += 1
elif num3 > 10 and num3 % 2 == 0:
    count += 1

print ("number of positive values:",count)

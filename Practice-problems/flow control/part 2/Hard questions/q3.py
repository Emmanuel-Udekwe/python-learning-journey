# ask user three true/false questions and count how many are true
x = str(input("Do you love God? (true/false):")).lower()
y = str(input("Do you love the devil (true/false):")).lower()
z = str(input("Are you a male? (true/false):")).lower()

# count how many are true
true_count = 0
if x == "true":
    true_count += 1
if y == "true":
    true_count += 1
if z == "true":
    true_count += 1

# print the correct result based on the number of true answers
if true_count == 3:
    print ("All true")  
elif true_count == 2:
    print ("Two true")
elif true_count == 1:
    print ("one true")  
else:
    print ("none true")                 


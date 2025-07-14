# dynamic username generator (basic)
# generate a username using first 3 letters of first name and full last
first_name = str(input("enter your first name:"))
last_name = str(input("enter your last name:"))
print ("your username is:",first_name[:3] + last_name)
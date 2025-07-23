# check if a password is longer than 8 characters and not equal to "password123"
password = str(input("enter your password:"))
print (len(password) > 8 and password != "password123")
# check if a password is strong based on basic condition.
password = str(input("enter your password:"))
if (len(password) >= 8) and (password != password.lower()) and (password != password.upper()):
    print ("strong")
else:
    print ("weak")   
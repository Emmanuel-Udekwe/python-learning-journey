# check if an email address is valid (simplified version)
email = str(input("enter an email address:"))
if (("@" and ".") in email) and (email.index("@") < email.index(".")):
    print ("true")
else:
    print ("false")   
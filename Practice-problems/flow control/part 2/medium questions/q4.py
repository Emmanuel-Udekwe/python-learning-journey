# ask for username and password and check acesss
username = str(input("enter username:"))
password = str(input("enter password:"))
if (username == "Admin") and (password == "letmein"):
    print ("Access granted")
elif (username == "Admin") and (password != "letmein"):
    print ("wrong password")
else:
    print ("unknown user")    
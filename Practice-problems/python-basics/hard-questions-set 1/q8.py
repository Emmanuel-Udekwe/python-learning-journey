# ask for first name,last name,favourite number,combine into a username
first_name = str(input("enter your first name:"))
last_name = str(input("enter your last name:"))
fav_number = int(input("enter your favourite number:"))
username = first_name +"." + last_name + str(fav_number)
print ("your username is:",username)
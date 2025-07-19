# ask user for full name , address, city,state,zip and print formatted address using \n
full_name = str (input("enter your full name:"))
street_address = str (input("enter your street address:"))
city = str (input("enter your city:"))
state = str (input("enter your state:"))
zipcode = int(input("enter your zipcode:"))
print ("\nformatted address:\n")
print ("full name:",full_name)
print ("street address:",street_address)
print ("city:",city)
print("state:",state)
print("zipcode:",zipcode)
       
# METHOD 2

full_name = str (input("enter your full name:"))
street_address = str (input("enter your street address:"))
city = str (input("enter your city:"))
state = str (input("enter your state:"))
zipcode = int(input("enter your zipcode:"))
print ("\nformatted address:\n")
print (full_name + "\n" + street_address + "\n" + city + "\n" + state + "\n" + str(zipcode))
       
       
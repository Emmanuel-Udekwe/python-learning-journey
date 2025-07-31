# Cinema ticket checker: Access based on ticket and exact change status
ticket = str(input("do you have a ticket (yes/no): ")).lower()
exact_change = str(input("do you have the exact change (yes/no):")).lower()
if (ticket == "yes") and (exact_change == "yes"):
    print ("Enter cinema")
elif (ticket == "yes") and (exact_change == "no"):
    print ("need exact change")
elif (ticket == "no") and (exact_change == "yes"):
    print ("no entry without ticket")
else:
    print("NO ENTRY")    


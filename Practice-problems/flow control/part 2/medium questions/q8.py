# ask for age and voters ID status, and check voting eligibility
age = int(input("enter your age:"))
vic = str(input("do you have a voters id card? (yes/no):"))
if (age >= 18) and (vic.lower() == "yes"):
    print ("Eligible to vote")
elif (age >= 18) and (vic.lower() == "no"):
    print ("voters id required")
else:
    print ("Not eligible to vote")    



    
    


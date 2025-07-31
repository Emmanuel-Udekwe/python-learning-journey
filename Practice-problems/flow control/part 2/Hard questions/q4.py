# number classification: classify number by sign and whether its even or odd:
num1 = int(input("enter an integer:"))
if (num1 > 0) and (num1 % 2 == 0):
    print ("positive even")
elif (num1 > 0) and (num1 % 2 != 0):
    print ("positive odd")   
elif (num1 < 0) and (num1 % 2 == 0):
    print ("negative even")  
elif (num1 < 0) and (num1 % 2 != 0):  
    print ("negative even")  
elif num1 == 0:
    print ("zero")    
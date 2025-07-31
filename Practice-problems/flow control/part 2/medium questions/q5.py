# ask for temprature in celsius and print a descriptive message
temp = int(input("enter temperature in celsius:"))
if temp <= 0:
    print ("freezing")
elif 1 <= temp <= 20:
    print ("cold")    
elif 21 <= temp <= 30:
    print ("warm")  
else:
    print ("Hot")


# but if we are dealing with decimals....

temp = float(input("enter temperature in celsius:"))
if temp <= 0:
    print ("freezing")
elif temp <= 20:
    print("cold")  
elif temp <= 30:
    print("warm") 
else:
    print ("Hot")         
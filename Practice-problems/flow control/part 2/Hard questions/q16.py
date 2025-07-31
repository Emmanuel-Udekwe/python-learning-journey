# calculate shipping cost based on weight and distance
weight = float(input("enter item weight in kg:"))
distance = float(input("enter distance in km:"))
if weight < 1.0:
    if distance < 50.0:
        print ("cost is 5")
    else:
        print ("cost is 10")  
if weight >= 1:
    if distance < 50:
        print ("cost is 15")          
    else:
        print ("cost is 20")    
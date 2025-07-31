# calculate BMI and classify it
weight = float(input("enter your weight in kg:"))
height = float(input("enter your height in meters:"))
BMI = weight / (height * height)
if BMI < 18.5:
    print ("underweight")
elif 18.5 <= BMI < 25:
    print ("Normal weight")   
elif 25 <= BMI < 30:
    print ("Overweight")  
elif BMI >= 30:
    print ("obese")      


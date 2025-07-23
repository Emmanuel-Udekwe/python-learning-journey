# ask for three input
temp_celsius = float(input("enter a temperature in celsius:"))
humidity = int(input("enter humidity percentage:"))
wind_speed = float(input("enter wind speed value:"))
# check whether condition
print (15 <= temp_celsius <= 25) and (humidity < 70) and (not(wind_speed > 20))

#or 

# ask for three input
temp_celsius = float(input("enter a temperature in celsius:"))
humidity = int(input("enter humidity percentage:"))
wind_speed = float(input("enter wind speed value:"))
# check whether condition
pleasant = (15 <= temp_celsius <= 25) and (humidity < 70) and (not(wind_speed > 20))
print (pleasant)

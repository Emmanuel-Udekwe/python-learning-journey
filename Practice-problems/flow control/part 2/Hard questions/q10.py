# stay indoors or go out: suggest activity based on time and weather
hour = int(input("enter current hour (0-23):"))
raining = str(input("is it raining? (yes/no):")).lower()
if (hour >= 18) or (raining == "yes"):
    print ("stay indoors")
else:
    print ("enjoy the day!")    
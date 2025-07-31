# ask for the current hour and greet based on the time of the day.
hour = int(input("enter current hour (0-23):"))
if hour < 12:
    print ("good morning")
elif hour < 18:
    print ("good afternoon")  
else:
    print ("good evening")      
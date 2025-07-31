# ask the user for the current traffic light color, print what action to take based on the colour
traffic_color = str(input("enter current traffic color (red,yellow or green):")).lower()
if traffic_color == "green":
    print ("Go!")
elif traffic_color == "yellow":
    print ("slow down")
elif traffic_color == "red":
    print ("stop!")  
else:
    print ("invalid color")      
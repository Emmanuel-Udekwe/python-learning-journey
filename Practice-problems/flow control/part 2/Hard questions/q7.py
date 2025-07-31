# overtime pay calculator: calculate overtime pay if hours > 0
hourly_wage = float(input("enter hourly wage:"))
hours_worked = float(input("enter hours worked in a week:"))
if hours_worked > 40.0:
    print ("overtime pay is " + str(1.5 * (hours_worked - 40.0)))
else:
    print ("No overtime")    
# calculate ticket price based on age and day of the week
age = int(input("enter your age:"))
day_of_the_week = str(input("enter the day of the week:")).lower()
if (age < 5) or (age > 60):
    print ("ticket price is zero")
elif day_of_the_week == "tuesday":
    print ("ticket price is 10 (discount day)")
elif 5 <= age <= 18:
    print ("Ticket price is 12")  
else:
    print ("Ticket price is 15")


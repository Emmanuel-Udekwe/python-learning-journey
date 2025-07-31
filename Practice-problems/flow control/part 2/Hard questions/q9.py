# leap year check: determine if a year is a leap year using rules
leap_year = int(input("enter a leap year:"))
if (leap_year % 4 == 0) and (leap_year % 100 != 0) or (leap_year % 400 == 0):
    print ("leap year")
else:
    print ("not a leap year")    
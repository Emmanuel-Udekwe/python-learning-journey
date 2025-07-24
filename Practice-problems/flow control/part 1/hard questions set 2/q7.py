# ask for an integer year
year = int(input("enter a year:"))
# leap year  logic
print (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
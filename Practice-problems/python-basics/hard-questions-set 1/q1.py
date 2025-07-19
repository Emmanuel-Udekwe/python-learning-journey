# 1. tip calculator with formatting
# ask user for bill amount and tip percent, then calculate and print tip and total with currency formatting
bill_amount = float (input("enter the bill amount:"))
tip_percentage = float (input("enter the tip percentage:"))
tip = (tip_percentage/100) * bill_amount
total = bill_amount + tip
print ("tip: " + "$" + str(round(tip,2)))
print ("total: " + "$" + str(round(total,2)))
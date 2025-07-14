# ask the user for hours worked and hourly rate, then print gross pay
hours = int (input("how many hours do you work?"))
hourly_rate = float (input("whats your hourly rate?"))
gross_pay = hours * hourly_rate
print ("your gross pay is " + str(gross_pay))
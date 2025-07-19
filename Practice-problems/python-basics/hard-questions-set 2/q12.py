# currency converter (USD to EUR)
# convert USD to EUR using a fixed rate
USD = float(input("enter an amount in USD:"))
exchange_rate_in_euro = 0.92
converted = USD * exchange_rate_in_euro
print ("your amount in euro is: " + str(round(converted,2)) + " euros")

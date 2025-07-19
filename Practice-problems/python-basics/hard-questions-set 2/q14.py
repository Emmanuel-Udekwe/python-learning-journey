# ask for item name, quantity and unit price: then calculate and print summary
item = str(input("enter item's name:"))
quantity = int(input("enter quantity:"))
unit_price = float(input("enter unit price:"))
total_cost = unit_price * quantity
print ("formatted summary\n" + "item: " + item + " " + "|" + " Qty:" + str(quantity) + " | " + "unit price:" + " $" + str(unit_price) + " " + "| " + "Total: " + "$" + str(total_cost))






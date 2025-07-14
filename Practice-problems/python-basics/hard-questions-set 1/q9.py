# ask for item,unit price,quantity,replicate item and print total
item_name = str(input("enter item name:"))
unit_price = float(input("enter unit price:"))
quantity = int(input("enter the quantity:"))
total_cost = unit_price * quantity
print ("items:", ((item_name + " ") * 3))
print ("Total cost of " + str(quantity) + " " + item_name + ":" + " " "$" + str(round(total_cost,2)))
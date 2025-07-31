# ATM SIMULATION: Check if PIN is correct and if withdrawal amount is within balance
pin = int(input("enter your 4-digit pin:"))
account_balance = float(input("enter your account balance:"))
withdrawal_amount = int(input("enter withdrawal amount:"))
if (pin == 1234) and (withdrawal_amount <= account_balance):
    print ("withdrawal approved")
elif (pin == 1234) and (withdrawal_amount > account_balance):
    print ("insufficient funds")
else:
    print ("invalid pin")    

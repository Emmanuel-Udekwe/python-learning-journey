# ask for namw, hours, rate; calculate grosspay and print with message
name = str (input("what is your name?"))
hours = float (input("number of hours worked?"))
rate = float(input("rate per hour?"))
grosspay = hours * rate
print("Hello,emmanuel.You worked " + str(hours) + " hours at " + str(rate) + "/hr." + " Your grosspay is " + "$" + str(grosspay))
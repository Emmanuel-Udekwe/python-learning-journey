# ask if your user likes python and java, then report likes
q1 = str(input("do you like python (yes/no):")).lower()
q2 = str(input("do you like java (yes/no:")).lower()
if (q1 == "yes") and (q2 == "yes"):
    print("both liked")
elif (q1 == "yes") and (q2 == "no"):   
    print ("one liked")
elif (q1 == "no") and (q2 == "yes"):
    print ("one liked")
else:
    print ("none liked")   
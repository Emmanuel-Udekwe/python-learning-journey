# ask the user for a sentence and check if its long or short
sentence1 = str(input("enter a sentence:"))
if len(sentence1) > 20:
    print ("long sentence")
else:
    print ("short sentence")   
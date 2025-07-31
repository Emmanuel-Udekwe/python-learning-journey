# classify the case type of a given word.
word = str(input("enter a word:"))
if word.isupper():
    print ("ALL CAPS")
elif word.islower():
    print ("all lowercase")  
else:
    print ("mixed CASE")

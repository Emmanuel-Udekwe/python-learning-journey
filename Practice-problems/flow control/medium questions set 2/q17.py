# ask for a name and a character . print based on name length and character match
name = str(input("enter your name:"))
single_character = str(input("enter a single character:"))
print (not(len(name) < 5) or single_character == "x")
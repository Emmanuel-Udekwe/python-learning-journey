# ask the user to input three different words
word1 = str(input("enter first word:"))
word2 = str(input("enter second word:"))
word3 = str(input("enter third word:"))
# check the logic
print (len(word1) > len(word2)) and (word2 != word3) or (word1 == word3)
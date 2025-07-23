# ask for two words,check if they are not the same and both longer than 4 characters
word1 = str(input("enter first word:"))
word2 = str(input("enter second word:"))
print (word1 != word2) and (len(word1)> 4) and (len(word2) > 4)
# Ask the user for a word. Print:
# - The word
# - Its character count using len()
# - The word repeated 3 times using * wirh spaces in btw them
# - A message: "Your word has X characters and looks wild as: Word Word Word"
word1 = str (input("enter a word:"))
print ("the word you entered is:", word1)
print ("the word has " + str(len(word1)) + " characters")
print ("repeated 3 times: " + (word1 + " ") * 3)
print ("your word has " + str(len(word1)) + " characters and looks wild as: ",(word1 * 3))



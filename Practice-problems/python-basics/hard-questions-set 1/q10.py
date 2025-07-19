# work with string: print first,last characters,length and replicate the message
message = "HELLO from the world of python!"
print("the first character of the message is:",message[:1])
print ("the last character of the message is:",message[-1:])
print ("the length of the message contains " + str(len(message)) + " characters")
print("message 3 times:",(message + " " )*3)
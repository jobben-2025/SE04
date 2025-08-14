#https://playground.wbscod.in/python/python-basics/1
#Strings: Basics

#Step 1:
#Create a variable with your name.
name = "John"

#Write a variable name message store inside a sentence like : "Hello, [name]! Welcome to Python."
message= "Hello, "+ name +"! Welcome to Python"

#Print message.
print( message)

#Step 2:
#Create a variable named char_in_message and store inside the number of characters in message.
char_in_message = len(message)

#Print char_in_message.
print(char_in_message)

#Create a variable named o_in_message and store the number of letters o in the message.
o_in_message = message.count('o')

#Print o_in_message.
print(o_in_message)

#Create a variable named vowels_in_message and set it's value to 0.
vowels_in_message = 0

#Create a variable name vowels = "aeiou" .
vowels = "aeiou"

#Use a for loop to iterate over each character in message, and if the character is in vowels update the vowels_in_message variable by adding 1 to the previous value.
for char in message:
    if char in vowels: vowels_in_message = vowels_in_message +1

#Print vowels_in_message.
print("Vowels in message: ", vowels_in_message)

#Step 3:
#Update the message replacing "Python" for "Javascript".
print("Original message: ", message)

#Print the updated message.
print("Replaced Python with Javascript: ", message.replace("Python", "Javascript"))




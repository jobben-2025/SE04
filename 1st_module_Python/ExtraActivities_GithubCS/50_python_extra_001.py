#Strings

#String Basics

### Step 1:
#1.  Create a variable with your name "inside as value".
name = "Ben"
    
#2.  Write a variable name `message` store inside a sentence like : `"Hello, [name]! Welcome to Python."`
message = "Hello, {}! Welcome to Python"        #full message in variable, use empty placeholder

#3.  Print `message`.
print(message.format(name))                     #using format and the filling variable for first empty placeholder

### Step 2:

#1.  Create a variable named `char_in_message` and store inside the number of characters in `message`.
char_in_message = len(message)    

#2.  Print `char_in_message`.
print("Number of characters in the word message:", char_in_message)

#3.  Create a variable named `o_in_message` and store the number of letters `o` in the `message`.
look_for = 'o'
o_in_message = message.lower().count(look_for)

#4.  Print `o_in_message`.
print("This many times counted o in message: ", o_in_message)

#5.  Create a variable named `vowels``_in_message` and set it's value to `0`.
vowels_in_message = 0

# You can print the new variable to see its value.
print("Variable named vowels_in_message has a value of:", vowels_in_message)
    
#6.  Create a variable name `vowels = "aeiou"` .
vowels = "aeiou"

#7.  Use a `for` loop to iterate over each character in message, and if the character is in `vowels` 
# update the `vowels_in_message` variable by adding 1 to the previous value.
for char in message:
    if char in vowels: vowels_in_message = vowels_in_message +1

#8.  Print `vowels_in_message`.
print("Found so many vowels in message: ", vowels_in_message)
print("Amount of chars_in_message", char_in_message)    

### Step 3:

#1.  Update the `message` replacing `"Python"` for `"Javascript"`.
message = message.format(name)                  #in tasks before just replaced temporary, now permanent
#print(message)
message = message.replace("Python", "Javascript")

#2.  Print the updated `message`.
print(message)





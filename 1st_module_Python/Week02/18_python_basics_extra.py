#01 String manipulation

name = "alice smith"
welcome_message = "Welcome to Stringville!"


#1. Capitalize user's name and surname on first letter
#title method does capitalize every first letter of each word of a string/variable
name = name.title()
print(name)

#2. Extract the first and last name separately
namelist = name.rsplit(" ")         #Splits the string at the specified separator, and returns a list
print(namelist[0])                  #from https://www.w3schools.com/python/python_strings_methods.asp
print(namelist[1])


#3. Count how many letters are in the name (excluding spaces)
#firstname_count = namelist[0].count()
#for c in namelist:
#surname_count = namelist[1].count()
print("There are so many characters in the full name:", str(len(namelist[0]+namelist[0])))


#4. Count how many letters are in the welcome message
print("There is this amount of letters in the welcome message:", len(welcome_message))


#02 String methods

#1. Check if the name contains the letter 's'
if "s" in name: print("There is at least one s in the given name.")


#2. Replace "Stringville" in the welcome message with another location (e.g. "Python City")
print("Replaced Stringville:", welcome_message.replace("Stringville", "Python City"))

#3. Capitalize the whole welcome message
print("Capitalized all letters:", welcome_message.upper())

#4. Lowercase the whole welcome message
print("Lowercased:", welcome_message.lower())

#5. Capitalize first letter of each word in welcome message
print("Capitalized:", welcome_message.title())


#6. Count how many occurences of "i" happen on the welcome message
#for "i" in welcome_message: 
w_message_count_i = welcome_message.count("i")
print("There are this many occurences of i inside the welcome message:", w_message_count_i)



#03 Joining Strings

#1. Create a final welcome message like: "Hello Alice Smith! Welcome to Python City!"
print(f"Hello {namelist[0]} {namelist[1]}! {welcome_message.replace("Stringville", "Python City")}")

#2. Bonus: Create a multi-line message using \n
print("This is part of an\nmultiline output displayed in the terminal.")




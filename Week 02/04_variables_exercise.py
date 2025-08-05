# Step 1: Create variables:
#Create a variable named name and assign your name as a string.
#Create a variable named age and assign your age as a number.
#Create a variable named height and assign your height in meters as a float.

name = str("Ben")
age = int(41)
height = float(188.3)

# Step 2: Print the variables:
#Use the print() function to display each variable’s value
print(name, age, height)
print()

# Step 3: Check the type of the variables:
#Print the type of each variable using the type() function.
print(type(name))
print(type(age))
print(type(height))

# Step 4: Casting
#Convert the age variable to a string and assign it to a new variable called age_str.
#Print a sentence that combines name and age_str. Example: "My name is Alice and I am 25 years old."
age_str = str(age)
print("My name is " + name + " and I am " + age_str)
#print("My name is " & name & " and I am " & age & " years old.")
#print(name, age)

# Bonus: Global Variable (Bonus)
#Create a variable named global_message outside a function and assign a message.
#Inside a function, use the global keyword to modify the global_message variable.
#Print the modified message after calling the function

global_message = "This is a global message"
print(global_message)

def test_function():
    global global_message
    global_message = "That should be the new global message"

test_function()
print(global_message)



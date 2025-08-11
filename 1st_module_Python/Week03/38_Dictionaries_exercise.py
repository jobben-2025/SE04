# 1. Create and Print a Dictionary
#Create a dictionary representing a person with keys such as "name", "age", and "city".
#Print the entire dictionary to the screen
my_dict = {
    "name": "John",
    "age": 41,
    "city": "Frankfurt"
    }
print("Initial dict: ", my_dict)

# 2. Access Dictionary Elements
#Print the value associated with the key "name" using square brackets.
print("Name: ", my_dict["name"])
#Use the get() method to safely retrieve the value for a key that might not exist (e.g., "email"), providing a default value.
maybe_key = my_dict.get("mail", "no email registered")
print("Email:", maybe_key)
#Print all keys, values, and items of the dictionary using keys(), values(), and items() methods
print("All keys printed: ", my_dict.keys())
print("All values printed: ", my_dict.values())
print("All items printed: ", my_dict.items())

# 3. Check for Key Existence
#Check if the key "age" exists in the dictionary using the in keyword.
#Print a message based on whether the key is found or not
print("There is a key 'age' in my_dict: ", "age" in my_dict)

# 4. Change and Update Dictionary Elements
#Update the value associated with "city" directly by assignment.
#Use the update() method to change multiple key-value pairs or add new ones (e.g., add "occupation": "Engineer").


# 5. Add New Items to the Dictionary
#Add a new key-value pair (e.g., "country": "USA") using direct assignment.
#Use update() to add another new key-value pair (e.g., "hobby": "cycling").


# 6. Remove Items from the Dictionary
#Remove an item by key using pop() and print the removed value.
#Use popitem() to remove the last inserted key-value pair, and print the pair removed.
#Delete a specific key-value pair using the del keyword.
#Clear the entire dictionary using clear() and print the empty dictionary


# 7. Copy a Dictionary
#Create a shallow copy of your dictionary using the copy() method or dict() constructor.
#Modify the original dictionary and show that the copy remains unchanged


# 8. Using setdefault()
#Use setdefault() to retrieve the value of a key that exists, and then for a key that doesn’t exist, adding it with a default value.
#Print the dictionary to observe changes






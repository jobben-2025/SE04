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
my_dict["city"] = "Stuttgart"
print("update city by assignment: ", my_dict)

#Use the update() method to change multiple key-value pairs or add new ones (e.g., add "occupation": "Engineer").
my_dict.update({"name":"John Cena", "age":"35", "city":"Belarus"})
print("using update method: ", my_dict)

# 5. Add New Items to the Dictionary
#Add a new key-value pair (e.g., "country": "USA") using direct assignment.
my_dict["country"] = "USA"
print("add new key pair using assignment: ", my_dict)

#Use update() to add another new key-value pair (e.g., "hobby": "cycling").
my_dict.update({"hobbies":"cycling"})
print("added new pair using update method ", my_dict)

# 6. Remove Items from the Dictionary
#Remove an item by key using pop() and print the removed value.
popped = my_dict.pop("name")
print(popped)
print("Dict after popping: ", my_dict)

#Use popitem() to remove the last inserted key-value pair, and print the pair removed.
removed = my_dict.popitem()
print("popped item: ", removed)
print("Dict after popping last item: ", my_dict)

#Delete a specific key-value pair using the del keyword.
del my_dict["country"]
print("Deleted country using del method: ", my_dict)

#Clear the entire dictionary using clear() and print the empty dictionary
my_dict.clear()
print("My dict after clearing: ", my_dict)

# 7. Copy a Dictionary
my_dict = {                         #create old dictionary for further code below
    "name": "John",
    "age": 41,
    "city": "Frankfurt"
    }

#Create a shallow copy of your dictionary using the copy() method or dict() constructor.
my_dict_copy = my_dict.copy()
my_dict_const = dict(my_dict)

#Modify the original dictionary and show that the copy remains unchanged
my_dict["age"] = 55
print("Original: ", my_dict)
print("Copy: ", my_dict_copy)
print("Constructed: ", my_dict_const)

# 8. Using setdefault()
#Use setdefault() to retrieve the value of a key that exists, and then for a key that doesn’t exist, adding it with a default value.
age_value = my_dict.setdefault("age", "20")
nation_value = my_dict.setdefault("nationality", "German")

#Print the dictionary to observe changes
print("Using set default 20 on age: ", age_value, nation_value)



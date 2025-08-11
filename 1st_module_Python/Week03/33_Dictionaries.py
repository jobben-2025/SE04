# Creating a dictionary to represent a person
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

# Printing the entire dictionary
print("Person dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Changing a value
person["age"] = 31
print("Updated age:", person["age"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("Added email:", person)

# Removing a key-value pair
del person["city"]
print("After removing city:", person)


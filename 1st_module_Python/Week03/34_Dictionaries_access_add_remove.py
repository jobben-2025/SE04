# dictionary_operations_demo.py

# Create an example dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial Dictionary:", my_dict)

# Accessing elements
print("\n--- Accessing Elements ---")
print("Using square brackets, name:", my_dict["name"])
print("Using get(), country:", my_dict.get("country", "Not Found"))
print("All keys:", list(my_dict.keys()))
print("All values:", list(my_dict.values()))
print("All items:", list(my_dict.items()))
print("'age' in dictionary?", "age" in my_dict)

# Changing elements
print("\n--- Changing Elements ---")
my_dict["age"] = 31  # item assignment
print("After changing age:", my_dict)
my_dict.update({"city": "Boston", "email": "alice@example.com"})
print("After update():", my_dict)

# Adding elements
print("\n--- Adding Elements ---")
my_dict["country"] = "USA"  # new key assignment
print("After adding country:", my_dict)
my_dict.update({"occupation": "Engineer"})
print("After adding occupation with update():", my_dict)

# Removing elements
print("\n--- Removing Elements ---")
removed_age = my_dict.pop("age", None)
print("Removed age value:", removed_age)
print("Dictionary after pop():", my_dict)

last_item = my_dict.popitem()
print("Popped last item:", last_item)
print("Dictionary after popitem():", my_dict)

# Adding more items for deletion demonstration
my_dict["hobby"] = "cycling"
print("\nBefore deletion:", my_dict)
del my_dict["city"]
print("After del my_dict['city']:", my_dict)

my_dict.clear()
print("After clear():", my_dict)

# Note: You can also delete the entire dictionary with 'del my_dict',
# but then my_dict will no longer exist, so further operations would fail.

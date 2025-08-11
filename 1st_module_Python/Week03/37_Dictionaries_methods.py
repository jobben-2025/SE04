# Create an initial dictionary
d = {"name": "Alice", "age": 30, "city": "New York"}
print("Initial dictionary:", d)

# clear()
temp_d = d.copy()  # Copy to preserve original for further demonstration
temp_d.clear()
print("After clear():", temp_d)

# copy()
copied_d = d.copy()
print("Copied dictionary using copy():", copied_d)

# fromkeys()
keys = ["a", "b", "c"]
new_d = dict.fromkeys(keys, 0)
print("Dictionary from keys using fromkeys():", new_d)

# get()
name_value = d.get("name")
missing_value = d.get("missing_key", "Default")
print("Value of 'name' using get():", name_value)
print("Missing key returns default using get():", missing_value)

# items()
items_list = list(d.items())
print("Items as list of tuples:", items_list)

# keys()
keys_list = list(d.keys())
print("Keys as list:", keys_list)

# pop()
age = d.pop("age")
print("Popped 'age':", age)
print("Dictionary after pop():", d)

# popitem()
last_item = d.popitem()
print("Popped last item using popitem():", last_item)
print("Dictionary after popitem():", d)

# setdefault()
# Reset dictionary for further demonstration
d = {"name": "Alice", "age": 30}
age_value = d.setdefault("age", 40)  # 'age' key exists, so returns existing value
country_value = d.setdefault("country", "USA")  # 'country' key doesn't exist, so sets and returns "USA"
print("setdefault existing key 'age':", age_value)
print("setdefault new key 'country':", country_value)
print("Dictionary after setdefault():", d)

# update()
d.update({"city": "Boston", "occupation": "Engineer"})
print("After update():", d)

# values()
values_list = list(d.values())
print("Values as list:", values_list)

# Create a set with some initial items
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Accessing items:
# Membership testing
if "apple" in fruits:
    print("Apple is in the set.")

# Iterating over items
print("Iterating over set items:")
for fruit in fruits:
    print(fruit)

# Adding items:
fruits.add("date")  # Adding a single item
print("\nAfter adding 'date':", fruits)

more_fruits = {"elderberry", "fig", "grape"}
fruits.update(more_fruits)  # Adding multiple items
print("After updating with more fruits:", fruits)

# Removing items:
fruits.remove("banana")  # Remove 'banana'; error if not found
print("\nAfter removing 'banana':", fruits)

fruits.discard("kiwi")  # Attempt to remove 'kiwi', no error if not present
print("After discarding 'kiwi' (which may not be present):", fruits)

# Using pop to remove an arbitrary item
removed = fruits.pop()
print("\nAfter pop(): removed", removed)
print("Set now:", fruits)

# Clearing the set
fruits.clear()
print("\nAfter clear():", fruits)           #output will display 'set()'

# 1. Creating a Set
# Sets are written with curly brackets {} or the set() constructor.
my_set = {"apple", "banana", "cherry", "apple"}  # Duplicate "apple" will be removed automatically
print("Initial set:", my_set)

# 2. Unordered Nature
# The order of elements in the printed set may vary.
print("Accessing set elements (unindexed):")
for item in my_set:
    print(item)
# 3. Unchangeable Items
# Attempting to change an individual element will result in an error.
#my_set[0] = "orange"  # This will raise an error because sets are unindexed.

# 4. Adding and Removing Items
# Although individual items cannot be changed, you can add or remove items from the set.
my_set.add("date")
print("After adding 'date':", my_set)

my_set.remove("banana")
print("After removing 'banana':", my_set)

# remove() raises an error if item doesn't exist
#my_set.remove('papaya')

# Using discard() to remove an item that might not be present:
my_set.discard("kiwi")  # Does nothing if 'kiwi' is not in the set, no error raised.

# 5. Membership Testing
if "cherry" in my_set:
    print("'cherry' is in the set")
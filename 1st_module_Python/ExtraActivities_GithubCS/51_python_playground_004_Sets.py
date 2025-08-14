#https://playground.wbscod.in/python/python-sets/1
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
print("\nAfter clear():", fruits)


# Define two sample sets
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "date", "elderberry"}

print("Set A:", set_a)
print("Set B:", set_b)

# 1. Union
# Using union() - returns a new set with elements from both
union_set = set_a.union(set_b)
print("\nUnion of Set A and Set B:", union_set)

# Using update() - modifies set_a to include elements from set_b
set_a.update(set_b)
print("Set A after update with Set B:", set_a)

# Reset set_a for further operations
set_a = {"apple", "banana", "cherry"}

# 2. Intersection
intersection_set = set_a.intersection(set_b)
print("\nIntersection of Set A and Set B:", intersection_set)

# 3. Difference
difference_set = set_a.difference(set_b)
print("\nDifference (Set A - Set B):", difference_set)

# Also demonstrate the opposite difference
difference_set_b = set_b.difference(set_a)
print("Difference (Set B - Set A):", difference_set_b)

# 4. Symmetric Difference
sym_diff_set = set_a.symmetric_difference(set_b)
print("\nSymmetric Difference between Set A and Set B:", sym_diff_set)


# Initialize two sets
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "date", "elderberry"}

print("Initial sets:")
print("set_a:", set_a)
print("set_b:", set_b)

# Using add()
set_a.add("fig")
print("\nAfter adding 'fig' to set_a:", set_a)

# Using discard() and remove()
set_a.discard("banana")  
print("After discarding 'banana' from set_a:", set_a)

# discard() does not raise an error if element not found
set_a.discard("kiwi")  
print("After attempting to discard 'kiwi' (not present):", set_a)

try:
    set_a.remove("cherry")
    print("After removing 'cherry' from set_a:", set_a)
except KeyError:
    print("'cherry' was not found in set_a to remove")

# Using copy()
set_c = set_b.copy()
print("\nCopy of set_b into set_c:", set_c)

# Using difference()
diff = set_b.difference(set_a)
print("\nDifference set_b - set_a:", diff)

# Using difference_update()
# Remove items from set_b that are also in the given set
set_b.difference_update({"banana", "fig"})
print("set_b after difference_update with {'banana', 'fig'}:", set_b)

# Reset sets for further operations
set_a = {"apple", "banana", "cherry", "fig"}
set_b = {"banana", "date", "elderberry", "fig"}

# Using intersection()
intersect = set_a.intersection(set_b)
print("\nIntersection of set_a and set_b:", intersect)

# Using intersection_update()
set_a.intersection_update(set_b)
print("set_a after intersection_update with set_b:", set_a)

# Reinitialize sets for union and update demonstration
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "date", "elderberry"}

# Using union()
uni = set_a.union(set_b)
print("\nUnion of set_a and set_b:", uni)

# Using update()
set_a.update(set_b)
print("set_a after update with set_b:", set_a)

# Using symmetric_difference()
sym_diff = set_a.symmetric_difference({"banana", "cherry"})
print("\nSymmetric difference of set_a and {'banana', 'cherry'}:", sym_diff)

# Using symmetric_difference_update()
set_a.symmetric_difference_update({"apple", "fig", "grape"})
print("set_a after symmetric_difference_update with {'apple', 'fig', 'grape'}:", set_a)

# Using pop()
popped_element = set_a.pop()
print("\nPopped element from set_a:", popped_element)
print("set_a after pop:", set_a)

# Checking relational methods: issubset, issuperset, isdisjoint
set_x = {1, 2}
set_y = {1, 2, 3, 4}

print("\nset_x:", set_x)
print("set_y:", set_y)
print("set_x is subset of set_y:", set_x.issubset(set_y))
print("set_y is superset of set_x:", set_y.issuperset(set_x))
print("set_x is disjoint with {5, 6}:", set_x.isdisjoint({5, 6}))

#EXERCISE:
#  1. Create a Set


# 2. Check Membership


# 3. Add and Update Items


# 4. Remove Items


# 5. Set Operations 


# 6. In-place Set Operations


# 7. Relational Methods



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

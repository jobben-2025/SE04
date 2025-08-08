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

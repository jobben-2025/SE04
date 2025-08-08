# 1. Sorting
numbers = [5, 2, 9, 1, 5, 6]
print("Original list of numbers:", numbers)

# In-place sort (ascending)
numbers.sort()
print("Sorted in-place (ascending):", numbers)

# Sort in descending order using sorted()
desc_numbers = sorted(numbers, reverse=True)
print("Descending order (new list):", desc_numbers)

# 2. Copying
original_list = ["apple", "banana", "cherry"]
reference_list = original_list  # Passes reference, not a true copy
copy_list_1 = original_list.copy()  # Creates a shallow copy (new list in memory)
copy_list_2 = original_list[:] # Another way to create a shallow copy

# Modify the original to see the difference
original_list.append("date")
print("\nAfter appending 'date' to original_list:")
print("original_list:", original_list)
print("reference_list (points to same list):", reference_list)
print("copy_list_1 (separate list):", copy_list_1)
print("copy_list_2 (separate list):", copy_list_2)

# 3. Joining Lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b  # Concatenate
print("\nJoin with '+':", list_c)

# Using extend()
list_a.extend(list_b)
print("After list_a.extend(list_b):", list_a)

# Using a for ... in loop with append()
list_f = [100, 200]
list_g = [300, 400]
for item in list_g:
    list_f.append(item)
print("After for-loop append:", list_f)

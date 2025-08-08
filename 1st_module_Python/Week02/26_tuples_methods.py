# 1. Create a Tuple
my_tuple = ("apple", "banana", "cherry", "banana", "date", "banana")

# 2. Using the count() method
banana_count = my_tuple.count("banana")
print("The word 'banana' appears:", banana_count, "times in my_tuple.")

# 3. Using the index() method
first_banana_index = my_tuple.index("banana")
print("The first occurrence of 'banana' is at index:", first_banana_index)

# Trying index() on a value that does not exist will raise an error
# Uncomment the next line to see the error
# my_tuple.index("grape")